print("SHOPPING CART")
print("here are some categories")
list=["clothing","shoes","watches","books"]
print("select one from these categories:")
print("1=clothing")
print("2=shoes")
print("3=watches")
print("4=books")
print("enter yes to shop no to exit")
total=[]
cart=[]
b=input()
while(b=="yes"):
    print("select either a category or enter 0 to exit")
    c=int(input())
#c=category
    if(c==0):
        break
    if(c==1):
        print("select for girls or boys")
#a=gender
        a=input()
        if(a=="girls"):
            print("select 1 for tops-price 500")
            print("select 2 for leggings-price 500")
            print("select 3 for jeans-price 2000")
            print("discount offer is 10%")
        if(a=="boys"):
            print("select 4 for t-shirts-price 1000")
            print("select 5 for formal shirts-price 1000")
            print("select 6 for boys jeans-price 2000")
            print("discount offer is 10%")
        d=int(input())
        if(d==1):
            price=500
            k=price-float((price)*(0.1))
            print(float(k))
            cart.append("tops")
        if(d==2):
            price=500
            k=price-float((price)*(0.1))
            print(float(k))
            cart.append("leggings")
        if(d==3):
            price=2000
            k=price-float((price)*(0.1))
            print(float(k))
            cart.append("jeans")
        if(d==4):
            price=1000
            k=price-float((price)*(0.1))
            print(float(k))
            cart.append("t-shirts")
        if(d==5):
            price=1000
            k=price-float((price)*(0.1))
            print(float(k))
            cart.append("formal shirts")
        if(d==6):
            price=2000
            k=price-float((price)*(0.1))
            print(float(k))
            cart.append("boys jeans")
        total.append(k)
    if(c==2):
        print("select for girls or boys")
        e=input()
        if(e=="girls"):
            print("select 1 for adidas-price 6000")
            print("select 2 for nike-price 5000")  
            print("select 3 for reebok-price 6000")
            print("discount offer is 10%")
        if(e=="boys"):
            print("select 4 for adidas-price 10000")
            print("select 5 for nike-price 9000")
            print("select 6 for puma-price 6000")
            print("discount offer is 10%")
        f=int(input())
        if(f==1):
            price=6000
            g=price-float((price)*(0.1))
            print(float(g))
            cart.append("adidas")
        if(f==2):
            price=5000
            g=price-float((price)*(0.1))
            print(float(g))
            cart.append("nike")
        if(f==3):
            price=6000
            g=price-float((price)*(0.1))
            print(float(g))
            cart.append("reebok")
        if(f==4):
            price=10000
            g=price-float((price)*(0.1))
            print(float(g))
            cart.append("adidas")
        if(f==5):
            price=9000
            g=price-float((price)*(0.1))
            print(float(g))
            cart.append("nike")
        if(f==6):
            price=6000
            g=price-float((price)*(0.1))
            print(float(g))
            cart.append("puma")
        total.append(g)
    if(c==3):
        print("select for girls or boys")
        h=input()
        if(h=="girls"):
            print("select 1 for fastrack-price 5000")
            print("select 2 for titan-price 6000")  
            print("select 3 for timex-price 5000")
            print("discount offer is 10%")
        if(h=="boys"):
            print("select 4 for fastrack-price 7000")
            print("select 5 for titan-price 9000")
            print("select 6 for timex-price 6000")
            print("discount offer is 10%")
        i=int(input())
        if(i==1):
            price=5000
            j=price-float((price)*(0.1))
            print(float(j))
            cart.append("fastrack")
        if(i==2):
            price=6000
            j=price-float((price)*(0.1))
            print(float(j))
            cart.append("titan")
        if(i==3):
            price=5000
            j=price-float((price)*(0.1))
            print(float(j))
            cart.append("timex")
        if(i==4):
            price=7000
            j=price-float((price)*(0.1))
            print(float(j))
            cart.append("fastrack")
        if(i==5):
            price=9000
            j=price-float((price)*(0.1))
            print(float(j))
            cart.append("titan")
        if(i==6):
            price=6000
            j=price-float((price)*(0.1))
            print(float(j))
            cart.append("timex")
        total.append(j)
    if(c==4):
        print("select 1 for harry potter")
        print("select 2 for ignited minds")
        print("select 3 for wings of fire")
        print("select 4 for my truth")
        print("select 5 for my experience with truth")
        print("select 6 for INDIA2020")
        print("discount offer is 50%")
        k=int(input())
        if(k==1):
            price=5000
            l=price-float((price)*(0.5))
            print(float(l))
            cart.append("harry potter")
        if(k==2):
            price=6000
            l=price-float((price)*(0.5))
            print(float(l))
            cart.append("ignited minds")
        if(k==3):
            price=5000
            l=price-float((price)*(0.5))
            print(float(l))
            cart.append("wings of fire")
        if(k==4):
            price=7000
            l=price-float((price)*(0.5))
            print(float(l))
            cart.append("my truth")
        if(k==5):
            price=9000
            l=price-float((price)*(0.5))
            print(float(l))
            cart.append(" my experience with truth")
        if(k==6):
            price=6000
            l=price-float((price)*(0.5))
            print(float(l))
            cart.append("INDIA2020")
        total.append(l)
print("your cart consists of")
print(cart)
add=0
for i in range(0,len(cart)):
    add=add+total[i]
print("your total price is:")
print(add)

















