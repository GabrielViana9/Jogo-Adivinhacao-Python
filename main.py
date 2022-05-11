import random

hidden_number = random.randrange(1,101)
maximum_attempts = 100
number_of_attempts = 0

while maximum_attempts > 0:

   maximum_attempts -= 1
   number_of_attempts += 1
   print("Tentativa Número {}".format(number_of_attempts))

   attempts = int(input("Escolha um número entre 1 e 100: "))

   if (attempts < 1 or attempts > 100):
       print("Número inválido, Digite um número válido !!\n")
       continue

   win = (hidden_number == attempts)
   bigger = (attempts > hidden_number)
   smaller = (attempts < hidden_number)

   if (win):
       print("Você ganhou, Parabéns !!!")
       print("Você tentou {} vezes até ganhar !!".format(number_of_attempts))
       break

   else:
       if (bigger):
           print("Você errou sua escolha({}) foi maior que o número escondido !\n".format(attempts))
       elif (smaller):
            print("Você errou sua escolha({}) foi menor que o número escondido !\n".format(attempts))