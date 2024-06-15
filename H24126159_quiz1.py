Richter = float(input("Please input a Richter scale value: ")) #input a Richter scale value
energy = 10**(1.5*Richter+4.8) #the equation of energy and Richter
TNT = energy/(4.184*10**9) #One ton of exploded TNT yields 4.184*(10**9) Joules.
lunch = energy/2930200 #one nutritious lunch contains 2930200 Joules.
print("Richter scale value: ",Richter)
print("Equivalence in Joules: ",energy)
print("Equivalence in tons of TNT: ",TNT)
print("Equivalence in the number of nutritious lunches: ",lunch)