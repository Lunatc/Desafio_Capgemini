


# Função que calcula o número total de views
def calculadora(views, count):

  total = int(views);
  clicks = int(views/12);
  share = (clicks/20) * 3;
  views = share * 40;
  
  count += 1;
  print(count);
  total += total + views;

# A função funciona de forma recursiva, e ao chegar em 4 termina
  if count < 4:
    return calculadora(views, count); 
  
  return total;

amount = int(input("Insira o valor investido (reais):"))
print("Username is: ",amount)

views = amount * 30
count = 0

total = int(calculadora(views, count));

print("Alcance:",total);

