CREATE OR REPLACE FUNCTION contar_clientes_cadastrados_em_um_dia(p_data_em_que_cadastrar DATE)
RETURN NUMBER
IS
  total_clientes NUMBER;
BEGIN
  SELECT COUNT(*) INTO total_clientes
  FROM clientes
  WHERE TRUNC(data_cadastro) = TRUNC(p_data_em_que_cadastrar);

  RETURN total_clientes;
END contar_clientes_cadastrados_em_um_dia;
/

---------------------------------------
DECLARE
  total_clientes_em_um_dia NUMBER;
BEGIN
  total_clientes_em_um_dia := contar_clientes_cadastrados_em_um_dia(TO_DATE('2024-01-11', 'YYYY-MM-DD'));
  DBMS_OUTPUT.PUT_LINE('Total de clientes cadastrados em um dia: ' || total_clientes_em_um_dia);
END;
/
