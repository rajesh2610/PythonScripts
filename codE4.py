temperatures = [10,-20,-289,100];

def conv(deg):
    f = (deg*9)/5 + 32;
    return f;

#deg =float(input("input temperature in degrees nigger:" ));
for deg in temperatures:
 if deg >= -273.15 :
   print(conv(deg))
 else:
   print("How on earth is that possible");
