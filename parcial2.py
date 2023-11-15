class cinema():
    
    def __init__(self):
        self.empleados={"marta":"4589","luisa":"4567","ricardo":"9090"}
        self.peliculas={"peli1":"11.30am","peli2":"02.00pm","peli3":"04.30pm","peli4":"07.00pm"}
        self.alimento={"alimento1":"2000","alimento1":"4000","alimento1":"6000","alimento1":"8000"}
        self.prox=["proxima1","proxima2","proxima3","proxima4"]
        self.admicon=777
        self.tiv=[["peli1","peli2","peli3","peli4"]]
        self.tia=[["alimento1","alimento2","alimento3","alimento4"]]
        self.lp=[]
        self.la=[]
        self.cupones=0
        self.reserva=[]

        self.cont1=0
        self.cont2=0
        self.cont3=0
        self.cont4=0

        self.contcom1=0
        self.contcom2=0
        self.contcom3=0
        self.contcom4=0

        while True:
            if self.cupones==50:
                break
            self.cl=str(input("""
            si es empleado digite 0
            si es clieste:
            que cliente es usted
            .1frecuente .2visitante

            si es admin digite su contrasena"""))
            if self.cl=="0":
                self.empleado()
            if self.cl=="1":
                self.menu1()
            if self.cl=="2":
                self.menu2()
            else:
                if self.cl=="777":
                    self.admin()
        
    def menu1(self):
        self.fre={"lalo":"1234","jhon":"5674"}
        self.usua=input("digite usuario")
        self.contra=input("digite su contraseña")
        if self.usua in self.fre and self.fre[self.usua]==self.contra:
            self.accfree=input("""que desea hacer
            1.ver lista de peliculas
            2.comprar tikeds
            3.comprar comoda
            4.reserva de peliculas
            """)
            if self.accfree=="1":
                print(self.peliculas)
            if self.accfree=="2":
                print( self.peliculas)
                self.tk=input(" de que pelicula desea el tiket:1.peli1,2.peli2,3.peli3,4.peli4?")
                if self.tk=="1":
                    self.cont1=+1
                    print("a adquirido un tiked para la pelicula 1")
                if self.tk=="2":
                    self.cont2=+1
                    print("a adquirido un tiked para la pelicula 2")
                if self.tk=="3":
                    self.cont3=+1
                    print("a adquirido un tiked para la pelicula 3")
                if self.tk=="4":
                    self.cont4=+1
                    print("a adquirido un tiked para la pelicula 4")
                    
                self.cupones=+1
        
                
            if self.accfree=="3":
                self.tc=print(" que alimento desea:1.alimento,2.alimento2,3.alimento3,4.alimento4?")
                if self.tc=="1":
                    self.contcom1=+1
                    print("a adquirido el alimento 1")
                if self.tc=="2":
                    self.contcom2=+1
                    print("a adquirido el alimento 2")
                if self.tc=="3":
                    self.contcom3=+1
                    print("a adquirido el alimento 3")
                if self.tc=="4":
                    self.contcom4=+1
                    print("a adquirido el alimento 4")

            if self.accfree=="4":
                self.tc=print(" que pelicula desea reservar:1.proxima1,2.proxima2,3.proxima3,4.proxima4")
                print("usterd a reservado un tiked para la pelicula:", self.tc)
        
        else:
            print("usted no esta registrado")        
             

    def menu2(self):
            self.accfree=input("""que desea hacer
            1.ver lista de peliculas
            2.comprar tikeds
            3.comprar comoda
            """)
            if self.accfree=="1":
                print( self.peliculas)
            if self.accfree=="2":
                print( self.peliculas)
                self.tk=print(" de que pelicula desea el tiket:1.peli1,2.peli2,3.peli3,4.peli4?")
                if self.tk=="1":
                    self.cont1=+1
                    print("a adquirido un tiked para la pelicula 1")
                if self.tk=="2":
                    self.cont2=+1
                    print("a adquirido un tiked para la pelicula 1")
                if self.tk=="3":
                    self.cont3=+1
                    print("a adquirido un tiked para la pelicula 1")
                if self.tk=="4":
                    self.cont4=+1
                    print("a adquirido un tiked para la pelicula 1")
                    
                self.cupones=+1
        
                
            if self.accfree=="3":
                self.tc=print(" que alimento desea:1.alimento,2.alimento2,3.alimento3,4.alimento4?")
                if self.tc=="1":
                    self.contcom1=+1
                    print("a adquirido un tiked para la pelicula 1")
                if self.tc=="2":
                    self.contcom2=+1
                    print("a adquirido un tiked para la pelicula 2 ")
                if self.tc=="3":
                    self.contcom3=+1
                    print("a adquirido un tiked para la pelicula 3")
                if self.tc=="4":
                    self.contcom4=+1
                    print("a adquirido un tiked para la pelicula 4")

            
            
    def admin(self):
        self.lp.append(self.cont1)
        self.lp.append(self.cont2)
        self.lp.append(self.cont3)
        self.lp.append(self.cont4)
        self.tiv.append(self.lp)

        self.la.apped(self.contcom1)
        self.la.apped(self.contcom2)
        self.la.apped(self.concomt3)
        self.la.apped(self.contcom4)
        self.tia.append(self.la)
        print(self.tiv)
        print(self.tia)
        
    def reserv(self):
        self.n=input("digite su nombre")
        self.j=[]
        self.j.appsend(self.n)
        self.j.appsend(self.tc)
        

    def empleado(self):
        self.en=input("nombre")
        self.cen=input("cotraseña")
        if self.en in self.empleados and self.empleados[self.en]==self.cen:
            print("ustred a sido validado como empleado")
        else:
            print("usted no es un empleado")


        
a=cinema()
    

