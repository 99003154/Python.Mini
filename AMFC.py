class cal1:                                                                   
    def __init__(self, a):                                                   
        self.a = a;
    def ctof(self):
        #a is celsius
        #this function comes under temperature conversion
        print("conversion from celsius to fahrenheit is : %f" % ((((self.a*9)/5))+32));
    def ctok(self):
        #a is celsius
        #this function comes under temperature conversion
        print("conversion from celsius to kelvin is : %f" % (self.a + 273.15));
       
    def ftoc(self): 
        #a is fahrenheit
        #this function comes under temperature conversion
        print("conversion from fahrenheit to celsius is : %f" % ((((self.a-32)*5)/9)));
    def ftok(self):
        #a is fahrenheit
        #this function comes under temperature conversion
        print("conversion from fahrenheit to kelvin is : %f" % ((((self.a-32)*5)/9)+273.15));
    def ktoc(self):
        #a is kelvin 
        #this function comes under temperature conversion
        print("conversion from kelvin to celsius is : %f" % (self.a-273.15));
    def ktof(self):
        #a is kelvin
        #this function comes under temperature conversion
        print("conversion from kelvin to fahrenheit is : %f" % (self.a-273.15));
    def area_circle(self):
        #a is radius of the circle
        #this operation comes under measurements of different shapes
        print("area of the circle is : %f" % (3.147*self.a*self.a));
    def area_square(self):
        #a is side of the square
        #this operation comes under measurements of different shapes
        print("area of the square is : %f" % (self.a*self.a));
    def peri_square(self):
        #a is side of the square
        #this operation comes under measurements of different shapes
        print("perimeter of the square is : %f" % (4*self.a));
    def peri_circle(self):
        #a is radius of the circle
        #this operation comes under measurements of different shapes
        print("perimeter of the circle is : %f" % (2*3.147*self.a));
        
                                                
class cal2(cal1):                                                            
    def __init__(self, a, b):                                                
        super().__init__(a);                                                 
        self.b = b;                                                             
    def APY(self):
        #a is stated annual interest
        #b is number of times compounded
        #this function comes under banking 
        print("Annual Percentage Yield in Banking is : %f" % (((1+(self.a/self.b))**self.b-1)));
    def DIR(self):
        #a is monthly debt payment
        #b is gross monthly income
        #this function comes under banking 
        print("Debt to Income Ratio in Banking is : %f" % (self.a/self.b));
    def LV(self):
        #a is loan amount
        #b is value of collateral
        #this function comes under banking sector
        print("Loan to Value in Banking is : %f" % (self.a/self.b));
    def NII(self):
        #a is interest income
        #b is interest expense
        #this function comes under banking sector
        print("Net Interest Income in Banking is : %f" % (self.a-self.b));
    def LDR(self):
        #a is loans
        #b is deposit
        #this function comes under banking sector
        print("Loan to Deposit Ratio is : %f" % (self.a/self.b));
    def NIS(self):
        #a is interest income rate
        #b is interest expense rate
        #this function comes under banking sector
        print("Net Interest Spread in Banking is : %f" % (self.a-self.b));
    def NIM(self):
        #a is net interest income
        #b is avg earning assets
        #this function comes under banking sector
        print("Net Interest Margin in Banking is : %f" % (self.a/self.b));
    def profit(self):
        #a is selling price of a product
        #b is cost price of a product
        #this function comes under banking sector
        print("profit is : %f" % (self.a-self.b));
    def loss(self):
        #a is cost price of a product
        #b is selling price of a product
        #this function comes under banking sector
        print("loss is : %f" % (self.a-self.b));
    def area_triangle(self):
        #a is height of the triangle
        #b is base of the triangle
        #this operation comes under measurements of different shapes
        print("area of the triangle is : %f" % ((self.a*self.b)/2));
    def area_rectangle(self):
        #a is height of the rectangle
        #b is width of the rectangle
        #this operation comes under measurements of different shapes
        print("area of the rectangle is : %f" % (self.a*self.b));
    def peri_rectangle(self):
        #a is height of the rectangle
        #b is width of the rectangle
        #this operation comes under measurements of different shapes
        print("perimeter of the rectangle is : %f" % (2*(self.a+self.b)));


                                                                                                                                                               
superObj = cal1(50);                                                      
subObj = cal2(15, 10);                                                     
superObj.ctok();
superObj.ftoc();
superObj.ftok();
superObj.ktoc();
superObj.ktof();
superObj.area_circle();
superObj.area_square();
superObj.peri_square();
superObj.peri_circle();
subObj.ctof();                                                                
subObj.APY();
subObj.DIR();
subObj.LV();
subObj.NII();
subObj.NIS();
subObj.LDR();
subObj.NIM();
subObj.profit();
subObj.loss();
subObj.area_triangle();
subObj.area_rectangle();
subObj.peri_rectangle();
