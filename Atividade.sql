DELIMITER //

CREATE PROCEDURE LevantamentoDiario()
BEGIN
    -- Criação de uma tabela temporária para armazenar o resultado do levantamento diário
    CREATE TEMPORARY TABLE IF NOT EXISTS TempLevantamentoDiario (
        data_compra DATE,
        quantidade_total INT
    );

    -- Inicialização da data de início e fim para o levantamento
    DECLARE data_inicio DATE;
    DECLARE data_fim DATE;
    
    -- Ajuste a data de início e fim conforme necessário
    SET data_inicio = CURDATE();  -- Pode ser alterado para qualquer data específica
    SET data_fim = CURDATE();  -- A mesma data de início para um levantamento diário

    -- Loop para percorrer os dias e calcular a quantidade total de produtos comprados
    WHILE data_inicio <= data_fim DO
        INSERT INTO TempLevantamentoDiario (data_compra, quantidade_total)
        SELECT
            data_compra,
            SUM(quantidade) AS quantidade_total
        FROM
            tabela_compras
        WHERE
            data_compra = data_inicio;
        
        SET data_inicio = DATE_ADD(data_inicio, INTERVAL 1 DAY);
    END WHILE;

    -- Seleção do resultado final
    SELECT * FROM TempLevantamentoDiario;

    -- Limpeza da tabela temporária após o uso
    DROP TEMPORARY TABLE IF EXISTS TempLevantamentoDiario;
END //

DELIMITER ;
