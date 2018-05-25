program Matrix; 
{$APPTYPE CONSOLE} 

var 
j, k, i, Nrow, Ncolumn, N, imin, imax: Integer; 
W:array [1..13, 1..7] of Real; 
d:array [1..13] of Real; 
B:array [1..26] of Real; 
x, p, pmax, pmin: Real; 

begin 
  write('������� ���������� ����� � �������� ������� W:'); 
    readln(Nrow, Ncolumn); 
  write('������� ', Nrow, ' ��������/�� ������� d:'); 
  for j := 1 to Nrow do // ���� ������� d 
    read(d[j]); 
  //writeln(d); 
  for j:= 1 to Nrow do begin // ������� ������� 
    x:= 0.5; 
    for k:= 1 to Ncolumn do begin 
      W[j, k] := cos(d[j])*Exp(1/3*ln(x)); 
      x:= x + 0.2; 
    end; 
  end; 
  writeln('�������������� �������:');
  for j:= 1 to Nrow do begin // ����� ������� W 
    for k:= 1 to Ncolumn do 
      write(W[j, k]:5:1); 
    writeln; 
  end; 
  pmax:= 0; 
  imax:= 0; 
  pmin:= 0;  
  imin:= 0;
  p:= 1;
  for k:= 1 to Ncolumn do begin
    for j:= 1 to Nrow do
      p:= p*W[j][k];
    if p > pmax then begin
      pmax:= p;
      imax:= k;
    end;
    if (p < pmin) or (pmin = 0) then begin
      pmin:= p;
      imin:= k;
    end;
  end;
  //write('imin=',imin,' pmin=',pmin,' imax=',imax,' pmax=',pmax);
  i:= 1;
  for j:= 1 to Nrow do begin
    B[i]:= W[j][imin];
    i:= i + 1;
  end;
  for j:= 1 to Nrow do begin
    B[i]:= W[j][imax];
    i:= i + 1;
  end;
  N:= i - 1;
  writeln('�������������� ������ B:');
  for i:= 1 to N do
  write(B[i]:5:1);
end.