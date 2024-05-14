
import wx
import random

"""
    -class MyFrame                        88
        > __init__                        90
        > oninit                         100
        ----------
        > on_pedir                       253
        > on_doblar                      258
        > on_cerrar                      263
        > on_separar                     268
        > on_timer                       273
        > on_automatico                  291
        > on_autoPause                   299
        > on_leeRetardo                  319
        > on_croupier                    329
        > on_manualAuto                  345
        ---------------
        > inicializar                    382
        > manual                         427
        > realizaJugada                  443
        > final                          498
        > blackjack                      536
        > muestraManoJ                   582
        > muestraManoC                   591
============================================
    -pideApuesta                         600
        > __init__                       606
        > on_apuesta2                    639
        > on_apuesta10                   644
        > on:apuesta50                   649
============================================
    -Resultados
        > __init__                       661
        > on_autoOK                      687
============================================
    -ventanaBlackjack                    692
        > __init__                       698
        > on_cambiaColor                 741
============================================
    -nuevaPartida                        755
        > on_SI                          788
        > on_NO                          792
============================================
    -CartaBase                           801
        > __init__                       805
        > valor                          812
    -Carta(CartaBase)                    817
        > __init__                       818
        > figura                         822
        > palo                           833        
============================================
    -Estrategia                          844
        > __init__                       861
        > cuenta_carta                   869
        > apuesta                        881
        > juegada                        898
============================================
    -Mazo                                915
        > __init__                       920
        > reparte                        930
============================================
    -Mano                                946
        > __init__                       947
        > anadir                         956
        > separar                        964
        > __str__                        976
        > sePuedeSeparar                1014                      
        > valor                         1021
        > strEstado                     1036                 
============================================
    compruebaApuesta                    1045
============================================
    -MyApp                              1059
============================================
    -main                               1070   


"""

class MyFrame(wx.Frame):
        
    def __init__(self, *args, **kwds):
        self.estrategia=Estrategia(Mazo.NUM_BARAJAS)
        self.mazo=Mazo(Carta,self.estrategia)
        self.nPartidas=0 #numero de partidas
        self.balance=0 #balance total
        self.t=11 #tiempo
        self.tAuto=1500 #temporizador por defecto automatico
        self.tCroupier=self.tAuto #temporizador por defecto del croupier
        self.oninit(*args,**kwds)        

    def oninit(self,*args,**kwds):    
        # begin wxGlade: MyFrame.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.Maximize()
        self.SetTitle("BLACKJACK by D.H.P.")

        self.Fondo = wx.Panel(self, wx.ID_ANY)
        self.Fondo.SetBackgroundColour(wx.Colour(42, 164, 0))

        sizer_3 = wx.BoxSizer(wx.VERTICAL)

        sizer_4 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_3.Add(sizer_4, 1, 0, 0)

        self.temporizador = wx.StaticText(self.Fondo, wx.ID_ANY, "timer", style=wx.ALIGN_CENTER_HORIZONTAL)
        self.temporizador.SetBackgroundColour(wx.Colour(127, 255, 0))
        self.temporizador.SetFont(wx.Font(14, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Segoe UI"))
        sizer_4.Add(self.temporizador, 3, wx.EXPAND, 0)

        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.on_timer,self.timer)

        self.automatico = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.on_automatico, self.automatico)
        self.automatico.Stop()

        self.jugadasCroupier = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.on_croupier, self.jugadasCroupier)

        self.panel_1 = wx.Panel(self.Fondo, wx.ID_ANY)
        sizer_4.Add(self.panel_1, 1000, 0, 0)

        self.npartida = wx.StaticText(self.Fondo, wx.ID_ANY, "nPartidas", style=wx.ALIGN_CENTER_HORIZONTAL| wx.ST_NO_AUTORESIZE)
        self.npartida.SetBackgroundColour(wx.Colour(127, 255, 0))
        self.npartida.SetFont(wx.Font(14, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Segoe UI"))
        sizer_4.Add(self.npartida, 3, wx.EXPAND, 0)

        self.panel_25 = wx.Panel(self.Fondo, wx.ID_ANY)
        sizer_3.Add(self.panel_25, 1, wx.EXPAND, 0)

        sizer_9 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_3.Add(sizer_9, 4, wx.EXPAND, 0)

        self.panel_20 = wx.Panel(self.Fondo, wx.ID_ANY)
        sizer_9.Add(self.panel_20, 1, wx.EXPAND, 0)

        self.Croupier = wx.StaticText(self.Fondo, wx.ID_ANY, "MANO", style=wx.ALIGN_CENTER_HORIZONTAL | wx.ST_NO_AUTORESIZE)
        self.Croupier.SetBackgroundColour(wx.Colour(25, 92, 3))
        self.Croupier.SetForegroundColour(wx.Colour(255,255,255))
        self.Croupier.SetFont(wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Consolas"))
        sizer_9.Add(self.Croupier, 2, wx.EXPAND, 0)

        self.panel_24 = wx.Panel(self.Fondo, wx.ID_ANY)
        sizer_9.Add(self.panel_24, 1, wx.EXPAND, 0)

        self.panel_21 = wx.Panel(self.Fondo, wx.ID_ANY)
        sizer_3.Add(self.panel_21, 1, wx.EXPAND, 0)

        sizer_8 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_3.Add(sizer_8, 17, wx.EXPAND, 0)

        self.panel_22 = wx.Panel(self.Fondo, wx.ID_ANY)
        sizer_8.Add(self.panel_22, 1, wx.EXPAND, 0)

        self.Yo = wx.StaticText(self.Fondo, wx.ID_ANY, "MANO", style=wx.ALIGN_CENTER_HORIZONTAL | wx.ST_NO_AUTORESIZE)
        self.Yo.SetBackgroundColour(wx.Colour(25, 92, 3))
        self.Yo.SetForegroundColour(wx.Colour(255,255,255))
        self.Yo.SetFont(wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Consolas"))
        sizer_8.Add(self.Yo, 2, wx.EXPAND, 0)

        self.panel_23 = wx.Panel(self.Fondo, wx.ID_ANY)
        sizer_8.Add(self.panel_23, 1, wx.EXPAND, 0)

        self.panel_26 = wx.Panel(self.Fondo, wx.ID_ANY)
        sizer_3.Add(self.panel_26, 2, wx.EXPAND, 0)

        static_line_2 = wx.StaticLine(self.Fondo, wx.ID_ANY)
        static_line_2.SetBackgroundColour(wx.Colour(0, 0, 0))
        sizer_3.Add(static_line_2, 0, wx.EXPAND, 0)

        sizer_5 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_3.Add(sizer_5, 2, wx.EXPAND, 0)

        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_5.Add(sizer_1, 4, wx.EXPAND, 0)

        sizer_6 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_1.Add(sizer_6, 2, wx.EXPAND, 0)

        self.manualAuto = wx.ToggleButton(self.Fondo, wx.ID_ANY, "manual")
        sizer_6.Add(self.manualAuto, 23, wx.ALL | wx.EXPAND, 2)
        self.Bind(wx.EVT_TOGGLEBUTTON, self.on_manualAuto, self.manualAuto)

        self.autoPause = wx.ToggleButton(self.Fondo, wx.ID_ANY, "Pausar Auto")
        self.Bind(wx.EVT_TOGGLEBUTTON,self.on_autoPause, self.autoPause)
        sizer_6.Add(self.autoPause, 24, wx.ALL | wx.EXPAND, 2)

        sizer_7 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_1.Add(sizer_7, 1, wx.EXPAND, 0)

        self.leeRetardo = wx.Button(self.Fondo, wx.ID_ANY, "OK")
        self.Fondo.Bind(wx.EVT_BUTTON, self.on_leeRetardo, self.leeRetardo)
        sizer_7.Add(self.leeRetardo, 0, 0, 0)

        self.retardo= wx.TextCtrl(self.Fondo, wx.ID_ANY, "1500",)
        sizer_7.Add(self.retardo, 2, wx.ALL, 2)

        label_1 = wx.StaticText(self.Fondo, wx.ID_ANY, "<--introduzca \nretardo\nen ms", style=wx.ALIGN_CENTER_HORIZONTAL)
        label_1.SetBackgroundColour(wx.Colour(255, 255, 255))
        sizer_7.Add(label_1, 0, wx.ALL | wx.EXPAND, 2)

        self.panel_2 = wx.Panel(self.Fondo, wx.ID_ANY)
        sizer_5.Add(self.panel_2, 2, wx.EXPAND, 0)

        botones = wx.BoxSizer(wx.HORIZONTAL)
        sizer_5.Add(botones, 16, wx.ALL | wx.EXPAND, 0)

        self.pedir = wx.Button(self.Fondo, wx.ID_ANY, "P")
        self.pedir.SetFont(wx.Font(24, wx.SWISS, wx.NORMAL, wx.NORMAL, 0, "Franklin Gothic Medium Cond"))
        self.Bind(wx.EVT_BUTTON, self.on_pedir, self.pedir)
        botones.Add(self.pedir, 10, wx.ALL | wx.EXPAND, 0)

        self.doblar = wx.Button(self.Fondo, wx.ID_ANY, "D")
        self.doblar.SetFont(wx.Font(24, wx.SWISS, wx.NORMAL, wx.NORMAL, 0, "Franklin Gothic Medium Cond"))
        self.Bind(wx.EVT_BUTTON, self.on_doblar, self.doblar)
        botones.Add(self.doblar, 10, wx.ALL | wx.EXPAND, 0)

        self.cerrar = wx.Button(self.Fondo, wx.ID_ANY, "C")
        self.cerrar.SetFont(wx.Font(24, wx.SWISS, wx.NORMAL, wx.NORMAL, 0, "Franklin Gothic Medium Cond"))
        self.Bind(wx.EVT_BUTTON, self.on_cerrar, self.cerrar)
        botones.Add(self.cerrar, 10, wx.ALL | wx.EXPAND, 0)

        self.separar = wx.Button(self.Fondo, wx.ID_ANY, "S")
        self.separar.SetFont(wx.Font(24, wx.SWISS, wx.NORMAL, wx.NORMAL, 0, "Franklin Gothic Medium Cond"))
        self.Bind(wx.EVT_BUTTON, self.on_separar, self.separar)
        botones.Add(self.separar, 9, wx.ALL | wx.EXPAND, 0)
        self.separar.Disable()

        self.panel_8 = wx.Panel(self.Fondo, wx.ID_ANY)
        sizer_5.Add(self.panel_8, 6, wx.EXPAND, 0)

        self.cartelBalance = wx.StaticText(self.Fondo, wx.ID_ANY, "$", style=wx.ALIGN_CENTER_HORIZONTAL | wx.ST_NO_AUTORESIZE)
        self.cartelBalance.SetBackgroundColour(wx.Colour(236, 255, 26))
        self.cartelBalance.SetFont(wx.Font(9, wx.MODERN, wx.NORMAL, wx.NORMAL, 0, "Fixedsys"))
        sizer_5.Add(self.cartelBalance, 2, wx.ALIGN_BOTTOM, 0)

        self.Fondo.SetSizer(sizer_3)

        self.Layout()

        # end wxGlade

    def on_pedir(self,event):
        """pide carta al pulsar boton P""" 
        #print("pedir")
        self.realizaJugada("P")
        
    def on_doblar(self,event):
        """dobla al pulsar el boton D"""
        #print("doblar")
        self.realizaJugada("D")
        
    def on_cerrar(self,event):
        """cierra al pulsar el boton C"""
        #print("cerrar")
        self.realizaJugada("C")

    def on_separar(self,event): 
        """separa al pulsar el boton S"""
        #print("separar")
        self.realizaJugada("S")

    def on_timer(self,event):
        """
        Si no hay manos que pueden pedir para el contador.
        Si hay y el contador llega a cero, pide carta. 
        Si no ha llegado a cero resta 1 al contador
        """
        #print("ontimer")       
        if not all(self.manosJugador[x].estado!=0 for x in range(len(self.manosJugador))):
            if self.t==0:
                #print("timerEnd")
                self.t=10
                self.realizaJugada("P")
            else:
                self.t-=1
            self.temporizador.SetLabel(str(self.t))
        else:
            self.timer.Stop()

    def on_automatico(self,event): 
        """
        realiza la jugada indicada por estrategia
        """
        #print("on_automatico")
        if not all(self.manosJugador[x].estado!=0 for x in range(len(self.manosJugador))):
            self.realizaJugada(self.estrategia.jugada(self.manoCroupier.cartas[0], self.manosJugador[self.manoIndice].cartas))
    
    def on_autoPause(self,event): 
        """
        cuando pausa el automatico, habilita el cambio a manual y para
        el temporizador de automatico y del croupier. Cuando se da al play se
        reinician los temporizadores
        """
        #print(onautoPause)
        val=self.autoPause.GetValue()
        if val:
            self.automatico.Stop()
            self.jugadasCroupier.Stop()
            self.manualAuto.Enable()
            self.autoPause.SetLabel("Play Auto")
        else:
            if not all(self.manosJugador[x].estado!=0 for x in range(len(self.manosJugador))):
                self.automatico.Start(self.tAuto)
            else: self.jugadasCroupier.Start(self.tCroupier)
            self.manualAuto.Disable()
            self.autoPause.SetLabel("Pausar Auto")

    def on_leeRetardo(self, event):
        """
        cuando se pulsa OK se lee el retardo y se guarda en el valor del retardo
        """
        #print(onleeRetardo)
        texto = self.retardo.GetValue()
        if texto.isdigit():
            self.tAuto=int(texto)
            self.tCroupier=self.tAuto

    def on_croupier(self,event):
        """
        cuando es turno del croupier pide carta hasta tener un valor >=17.
        una vez esto ocurre llama el método final()
        """
        #print("croupier")
        self.automatico.Stop()
        self.muestraManoC()
        if self.manoCroupier.valor<17:
            #print (self.manoCroupier)
            self.manoCroupier.anadir(self.mazo.reparte()) # el croupier pide carta siempre que tenga menos de 17
            self.muestraManoC()
        else:
            self.jugadasCroupier.Stop()
            self.final()

    def on_manualAuto(self,event):
        """
        cuando se cambia de modo manual a automático, se dehabilitan los botones
        de jugadas y se habilitan los controles de la partida automática. también 
        cambia el nombre de la etiqueta

        cuando se cambia a manual se reestablecen los cambios excepto el boton
        de separar yse reestablece el temporizador del croupier al establecido
        por defecto.
        """
        val=self.manualAuto.GetValue()
        if val:
            self.manualAuto.SetLabel("Manual")
            self.manualAuto.Disable()
            #print("auto")
            self.pedir.Disable()
            self.doblar.Disable()
            self.cerrar.Disable()
            self.separar.Disable()
            self.leeRetardo.Enable()
            self.retardo.Enable()
            self.autoPause.Enable()
            self.automatico.Start(self.tAuto)
        else:
            self.tCroupier=1500
            self.manualAuto.SetLabel("Auto")
            self.autoPause.SetValue(False)
            #print("manual")
            self.pedir.Enable()
            self.doblar.Enable()
            self.cerrar.Enable()
            self.leeRetardo.Disable()
            self.retardo.Disable()
            self.autoPause.Disable()

            self.manual()

    def inicializar(self):
        """
        inicializa la partida, creando una mano para el croupier y otra para el
        jugador y reinicializa otras variables. A continuacion apareceel diálogo
        pidiendo la apuesta (en manual) o pide la apuesta a el objeto de estrategia.
        Después reparte dos cartas al jugador y una al cropier. Si el jugador tiene
        blackjack llama el método blackjack
        """
        self.manoCroupier=Mano()
        self.manoCroupier.nombre="Croupier"
        self.manosJugador=[]     # lista de las distintas manos del jugador
        self.manosJugador.append(Mano())
        self.manoIndice=0

        self.parcial=0 
        self.nPartidas+=1
        self.npartida.SetLabel(str(self.nPartidas))
        self.stringResultado=""

        if not self.manualAuto.GetValue():
            dialog = pideApuesta(self, frame=self)
            dialog.ShowModal()
            self.manosJugador[0].apuesta=dialog.apuesta
            dialog.Destroy()
        else:
            self.manosJugador[0].apuesta=self.estrategia.apuesta(2,10,50)
            self.automatico.Start(self.tAuto)

        self.manoCroupier.anadir(self.mazo.reparte())
        #print(self.manoCroupier)
        self.muestraManoC()

        self.manosJugador[0].anadir(self.mazo.reparte())
        self.manosJugador[0].anadir(self.mazo.reparte()) # reparte una carta al croupier y dos a la primera mano del jugador

        #print(self.manosJugador[0])
        self.muestraManoJ()

        if self.manosJugador[0].valor==21: # comprueba si hay blackjack
            self.pedir.Disable()
            self.doblar.Disable()
            self.cerrar.Disable()

            self.blackjack()

    def manual(self):
        """
        método que inicializa una partida para el modo manual
        """
        self.inicializar()
        if self.manosJugador[0].sePuedeSeparar:
            self.separar.Enable()
            self.pedir.Enable()
            self.doblar.Enable()
            self.cerrar.Enable()
        else:
            self.pedir.Enable()
            self.doblar.Enable()
            self.cerrar.Enable()
    
    
    def realizaJugada(self,jugada):
        """
        método que realiza las jugadas. tiene en cuenta que si deja de haber jugadas
        que puede hacer el jugador, inicia la partida del croupier. También, si tras
        realizar una acción se puede separar la mano, habilita el boton S.
        """
        self.t=11
        match jugada:
            case "P":
                self.manosJugador[self.manoIndice].anadir(self.mazo.reparte())
                if not all(self.manosJugador[x].estado!=0 for x in range(len(self.manosJugador))):
                    if self.manosJugador[self.manoIndice].estado!=0:
                        self.manoIndice+=1
                    if self.manosJugador[self.manoIndice].sePuedeSeparar:
                        self.separar.Enable
                else:
                    self.pedir.Disable()
                    self.doblar.Disable()
                    self.cerrar.Disable()
                    self.separar.Disable()
                    self.jugadasCroupier.Start(self.tCroupier)
            case "D":
                self.manosJugador[self.manoIndice].anadir(self.mazo.reparte())
                self.manosJugador[self.manoIndice].apuesta*=2
                if self.manosJugador[self.manoIndice].valor>21:
                    self.manosJugador[self.manoIndice].estado=2
                else: self.manosJugador[self.manoIndice].estado=1
                if not all(self.manosJugador[x].estado!=0 for x in range(len(self.manosJugador))):
                    self.manoIndice+=1
                    if self.manosJugador[self.manoIndice].sePuedeSeparar:
                        self.separar.Enable
                else:
                    self.pedir.Disable()
                    self.doblar.Disable()
                    self.cerrar.Disable()
                    self.separar.Disable()
                    self.jugadasCroupier.Start(self.tCroupier)              
            case "C":
                self.manosJugador[self.manoIndice].estado=1
                if not all(self.manosJugador[x].estado!=0 for x in range(len(self.manosJugador))):
                    self.manoIndice+=1
                    if self.manosJugador[self.manoIndice].sePuedeSeparar:
                        self.separar.Enable
                else:
                    self.pedir.Disable()
                    self.doblar.Disable()
                    self.cerrar.Disable()
                    self.separar.Disable()
                    self.jugadasCroupier.Start(self.tCroupier)
            case "S":
                self.manosJugador.extend(self.manosJugador[self.manoIndice].separar()) 
                del self.manosJugador[self.manoIndice]
                self.separar.Disable
        self.muestraManoJ()
         
    def final(self):
        """
        final de la partida en caso de que no haya blackjack. Contabiliza los
        resultados y los muestra en la ventana de diálogo Resultados. A continuación
        se pregunta en la ventana de diálogo nuevaPartida si se quiere jugar de nuevo,
        reinicializando la partida si es el caso. Si se juega en automático no 
        preguntará si se quiere jugar de nuevo
        """
        for mano in self.manosJugador:
            a=compruebaApuesta(mano.apuesta,mano.valor,self.manoCroupier.valor)
            self.parcial+=a
            self.balance+=a
            self.cartelBalance.SetLabel(str(self.balance)+"$")
            self.stringResultado=self.stringResultado+"* Croupier: "+str(self.manoCroupier.valor)+", "+mano.nombre+":"+str(mano.valor)+"-> "+ str(a)+"$\n"
        self.stringResultado=self.stringResultado+"Resultado de la partida: "+str(self.parcial)+"$\n"+"BALANCE: "+str(self.balance)+"$"
        if not self.manualAuto.GetValue():
            resultado = Resultados(self,t=5000)
            resultado.texto.SetLabel(self.stringResultado)
            resultado.ShowModal()
            resultado.Destroy()
            resultado.autoOK.Stop()
            self.nueva = nuevaPartida(None, wx.ID_ANY, "")
            self.nueva.ShowModal()
            val= self.nueva.val
            self.nueva.Destroy()
            if not val:
                self.Close()
            else:
                self.manual()
        else:
            resultado = Resultados(self,t=self.tAuto)
            resultado.texto.SetLabel(self.stringResultado)
            resultado.ShowModal()
            resultado.autoOK.Stop()
            resultado.Destroy()
            self.inicializar()


    def blackjack(self):
        """
        En caso de haber blackjack aparece la ventana ventanaBlackjack. En el resto
        del método actua de forma similar a final()
        """
        #print("blackjack")
        self.automatico.Stop()
        self.parcial=self.manosJugador[0].apuesta*1.5
        self.balance+=self.parcial
        self.stringResultado="**********************\n*** BLACKJACK **\n**********************\n"+self.stringResultado+"Resultado de la partida: "+str(self.parcial)+"$\n"+"BALANCE: "+str(self.balance)+"$"
        
        

        if not self.manualAuto.GetValue():
            self.cartelBalance.SetLabel(str(self.balance)+"$")
            self.bj = ventanaBlackjack(None, wx.ID_ANY, "",recompensa=(self.manosJugador[0].apuesta*1.5),t=5000)
            self.bj.ShowModal()
            self.bj.Destroy()
            self.bj.cambiaColor.Stop()
            resultado = Resultados(self,t=5000)
            resultado.texto.SetLabel(self.stringResultado)
            resultado.ShowModal()
            resultado.Destroy()
            self.nueva = nuevaPartida(None, wx.ID_ANY, "")
            self.nueva.ShowModal()
            val= self.nueva.val
            self.nueva.Destroy()
            if not val:
                self.Close()
            else:
                self.manual()
        else:
            
            self.cartelBalance.SetLabel(str(self.balance)+"$")
            self.bj = ventanaBlackjack(None, wx.ID_ANY, "",recompensa=(self.manosJugador[0].apuesta*1.5),t=1000)
            self.bj.ShowModal()
            self.bj.Destroy()
            self.bj.cambiaColor.Stop()
            resultado = Resultados(self,t=self.tAuto)
            resultado.texto.SetLabel(self.stringResultado)
            resultado.ShowModal()
            resultado.Destroy()
            
            resultado.Destroy()
            self.inicializar()

    def muestraManoJ(self):
        """
        muestra la mano del jugador
        """
        string=""
        for mano in self.manosJugador:
            string+=str(mano)+"\n"
        self.Yo.SetLabel(string)

    def muestraManoC(self):
        """
        muestra la mano del croupier
        """
        string=str(self.manoCroupier)
        self.Croupier.SetLabel(string)
            


class pideApuesta(wx.Dialog):
    """
    recibe como argumentos frame. Muestra tres botones con imágenes de fichas
    con las distintas apuestas. cuando pulsas una, devuelve el valor de la 
    apuesta e inicializa el temporizador
    """
    def __init__(self, *args, frame, **kwds):
        self.apuesta=10
        self.frame=frame

        # begin wxGlade: MyDialog.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_DIALOG_STYLE
        wx.Dialog.__init__(self, *args, **kwds)
        self.SetSize((496, 199))
        self.Center()
        self.SetTitle("dialog")

        sizer_2 = wx.BoxSizer(wx.HORIZONTAL)

        self.apuesta2 = wx.BitmapButton(self, wx.ID_ANY, wx.Bitmap("images/2chip.png", wx.BITMAP_TYPE_PNG))
        self.apuesta2.SetSize(self.apuesta2.GetBestSize())
        sizer_2.Add(self.apuesta2, 0, 0, 0)
        self.Bind(wx.EVT_BUTTON, self.on_apuesta2, self.apuesta2)

        self.apuesta10 = wx.BitmapButton(self, wx.ID_ANY, wx.Bitmap("images/10chip.png", wx.BITMAP_TYPE_ANY))
        self.apuesta10.SetSize(self.apuesta10.GetBestSize())
        sizer_2.Add(self.apuesta10, 0, 0, 0)
        self.Bind(wx.EVT_BUTTON, self.on_apuesta10, self.apuesta10)

        self.apuesta50 = wx.BitmapButton(self, wx.ID_ANY, wx.Bitmap("images/50chip.png", wx.BITMAP_TYPE_ANY))
        self.apuesta50.SetSize(self.apuesta50.GetBestSize())
        sizer_2.Add(self.apuesta50, 0, 0, 0)
        self.Bind(wx.EVT_BUTTON, self.on_apuesta50, self.apuesta50)

        self.SetSizer(sizer_2)
        

        self.Layout()
    
    def on_apuesta2(self,event):
        self.apuesta=2
        self.frame.timer.Start(1000)
        self.Close()
    
    def on_apuesta10(self,event):
        self.apuesta=10
        self.frame.timer.Start(1000)
        self.Close()

    def on_apuesta50(self,event):
        self.apuesta=50
        self.frame.timer.Start(1000)
        self.Close()
        # end wxGlade
            
class Resultados(wx.Dialog):
    """
        muestra el resultado de la partida. Recibe t como argumento, este es el tiempo
        que tarda en cerrarse automáticamente que es distinto entre el modo manual y el 
        automático. En automatico es el tAuto indicado por el jugador.
    """
    def __init__(self, *args,t, **kwds):
        self.t=t
        # begin wxGlade: MyDialog.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_DIALOG_STYLE
        wx.Dialog.__init__(self, *args, **kwds)
        self.Center()
        self.SetTitle("dialog")

        sizer_1 = wx.BoxSizer(wx.VERTICAL)

        self.texto = wx.StaticText(self, wx.ID_ANY, "",style=wx.ALIGN_CENTER_HORIZONTAL)
        self.texto.SetMinSize((400, 230))
        sizer_1.Add(self.texto, 0, 0, 0)

        self.button_OK = wx.Button(self, wx.ID_OK, "")
        self.button_OK.SetDefault()
        sizer_1.Add(self.button_OK, 0, wx.EXPAND, 0)

        self.SetSizer(sizer_1)
        sizer_1.Fit(self)

        self.SetAffirmativeId(self.button_OK.GetId())
        self.autoOK=wx.Timer(self)
        self.Bind(wx.EVT_TIMER,self.on_autoOK,self.autoOK)
        self.autoOK.StartOnce(self.t)
        self.Layout()
    def on_autoOK(self,event):
        #print("on_autoOK")
        self.Close()
        

class ventanaBlackjack(wx.Dialog):
    """
    ventana que avisa de que ha conseguido blackjack. Tiene un temporizador 
    que hace que cambie de color de amarillo a azul cada 500ms. También recibe t
    como argumento que indica su tiempo de vida.
    """
    def __init__(self, *args,recompensa,t, **kwds):
        self.color=0
        self.recompensa=recompensa
        self.t=t/500
        # begin wxGlade: MyDialog.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_DIALOG_STYLE
        wx.Dialog.__init__(self, *args, **kwds)
        self.Center()
        self.SetTitle("dialog")

        self.panel_14 = wx.Panel(self, wx.ID_ANY)
        self.panel_14.SetBackgroundColour(wx.Colour(255, 255, 0))

        sizer_4 = wx.BoxSizer(wx.HORIZONTAL)

        self.panel_2 = wx.Panel(self.panel_14, wx.ID_ANY)
        sizer_4.Add(self.panel_2, 1, wx.EXPAND, 0)

        sizer_5 = wx.BoxSizer(wx.VERTICAL)
        sizer_4.Add(sizer_5, 10, wx.EXPAND, 0)

        self.panel_1 = wx.Panel(self.panel_14, wx.ID_ANY)
        sizer_5.Add(self.panel_1, 1, wx.EXPAND, 0)

        label_1 = wx.StaticText(self.panel_14, wx.ID_ANY, "**********************\n*** BLACKJACK **\n**********************\nHA GANADO "+str(self.recompensa)+"$", style=wx.ALIGN_CENTER_HORIZONTAL)
        label_1.SetBackgroundColour(wx.Colour(255, 255, 255))
        label_1.SetFont(wx.Font(22, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, ""))
        sizer_5.Add(label_1, 6, wx.ALL | wx.EXPAND, 0)

        self.button_1 = wx.Button(self.panel_14, wx.ID_OK, "")
        sizer_5.Add(self.button_1, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 5)

        self.panel_4 = wx.Panel(self.panel_14, wx.ID_ANY)
        sizer_4.Add(self.panel_4, 1, wx.EXPAND, 0)

        self.panel_14.SetSizer(sizer_4)

        self.cambiaColor=wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.on_cambiaColor, self.cambiaColor)
        self.cambiaColor.Start(500)

        self.Layout()
        # end wxGlade
    def on_cambiaColor(self,event):
        #print("on_cambiaColor")
        if self.color%2==0:
            self.panel_14.SetBackgroundColour(wx.Colour(255, 255, 0))
            self.color+=1
        else:
            self.panel_14.SetBackgroundColour(wx.Colour(0, 25, 255))
            self.color+=1
        if self.color==self.t:
            self.cambiaColor.Stop()
            self.Close()
        self.panel_14.Refresh()
        # end wxGlade
#========================================================================================
class nuevaPartida(wx.Dialog):
    """
    pregunta si se quiere jugar una nueva partida.
    """
    def __init__(self, *args, **kwds):
        # begin wxGlade: nuevaPartida.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_DIALOG_STYLE
        wx.Dialog.__init__(self, *args, **kwds)
        self.Center()
        self.SetTitle("dialog")

        sizer_1 = wx.BoxSizer(wx.VERTICAL)

        label_1 = wx.StaticText(self, wx.ID_ANY, u"¿NUEVA PARTIDA?")
        label_1.SetFont(wx.Font(16, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, ""))
        sizer_1.Add(label_1, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)

        sizer_2 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_1.Add(sizer_2, 1, wx.EXPAND, 0)

        self.botSI = wx.Button(self, wx.ID_YES, "")
        sizer_2.Add(self.botSI, 1, 0, 0)
        self.Bind(wx.EVT_BUTTON, self.on_SI, self.botSI)


        self.botNO = wx.Button(self, wx.ID_NO, "")
        sizer_2.Add(self.botNO, 1, 0, 0)
        self.Bind(wx.EVT_BUTTON, self.on_NO, self.botNO)

        self.SetSizer(sizer_1)
        sizer_1.Fit(self)

        self.Layout()
    def on_SI(self,event):
        #print(onSI)
        self.val=True
        self.Close()
    def on_NO(self,event):
        #print(onNO)
        self.val=False
        self.Close()


#========================================================================================
#========================================================================================  

class CartaBase(object):
    """ Clase minimalista que representa una carta de la baraja
        Debería crearse una clase que herede de esta
    """
    def __init__(self, ind):
        """ Crea la carta con ese índice (0-51)
        :param ind: El índice de la carta
        """
        self.ind = ind

    @property
    def valor(self):
        """
        :return: Valor facial de la carta (1-10). Los ases devuelven 1.
        """
        return min(10, self.ind % 13 + 1)
class Carta(CartaBase):
    def __init__(self, ind):
        super().__init__(ind)
        self.ind=ind
    @property
    def figura(self):
        a=self.ind%13+1
        respuesta=str(a)
        if a==11:
            respuesta="J"
        elif a==12:
            respuesta="Q"
        elif a==13:
            respuesta="K"
        return respuesta
    @property
    def palo(self):
        """
        palo de la carta, 
        0-->picas; 1-->corazones; 2-->tréboles; 3-->diamantes
        """
        if self.ind in range(0,13):
            return "♠"
        elif self.ind in range(13,26):
            return "♥"
        elif self.ind in range(26,39):
            return "♣"
        else:
            return "♦"
#========================================================================================
class Estrategia(object):
    """ Clase que representa una estrategia de juego para el Blackjack
        Basada en el libro que muestra Alan en Resacón en las Vegas
    """
    # Matrices de estrategia: Filas suma de valores de cartas del jugador (ases = 1), columnas valor carta del croupier
    # Matriz para jugadas con 2 cartas del mismo valor (inicio fila 2)
    MATD = ['S' * 10, *['P' + 'S' * 6 + 'PPP'] * 2, 'P' * 4 + 'SS' + 'P' * 4, 'P' + 'D' * 8 + 'P',
            'P' + 'S' * 6 + 'PPP', 'P' + 'S' * 7 + 'PP', 'S' * 10, 'C' + 'S' * 5 + 'CSSC', 'C' * 10]
    # Matriz para jugadas con algún as (inicio fila 3, suma debe dividirse por 2)
    MATA = [*['P' * 4 + 'DD' + 'P' * 4] * 2, *['PPPDDD' + 'P' * 4] * 2, 'PP' + 'D' * 4 + 'P' * 4,
            'PC' + 'D' * 4 + 'CCPP', *['C' * 10] * 3]
    # Matriz para jugadas sin ases ni duplicados (inicio fila 4)
    MATN = [*['P' * 10] * 5, 'P' + 'D' * 5 + 'P' * 4, 'P' + 'D' * 8 + 'P', 'D' * 10,
            'P' * 3 + 'C' * 3 + 'P' * 4, *['P' + 'C' * 5 + 'P' * 4] * 4, *['C' * 10] * 5]
    # Vector de estrategia de conteo
    CONT = [-2, 2, 2, 2, 3, 2, 1, 0, -1, -2]

    def __init__(self, num_barajas):
        """ Crea e inicializa la estrategia
        :param num_barajas: Número de barajas del mazo utilizado en el juego
        """
        self.num_barajas = num_barajas
        self.num_cartas = 0
        self.cuenta = 0

    def cuenta_carta(self, carta):
        """ Este método se llama automáticamente por el objeto Mazo cada vez
            que se reparte una carta
        :param carta: La carta que se ha repartido
        """
        self.num_cartas += 1
        if self.num_cartas >= 52 * self.num_barajas:
            # Se ha cambiado el mazo
            self.num_cartas = 1
            self.cuenta = 0
        self.cuenta += Estrategia.CONT[carta.valor-1]

    def apuesta(self, apu_lo, apu_med, apu_hi):
        """ Indica la apuesta que se debe realizar dado el estado del juego.
            Elige entre 3 valores posibles (baja, media y alta)
        :param apu_lo: El valor de la apuesta baja
        :param apu_med: El valor de la apuesta media
        :param apu_hi: El valor de la apuesta alta
        :return: Uno de los 3 valores posibles de apuesta
        """
        barajas_restantes = self.num_barajas - self.num_cartas // 52
        true_count = self.cuenta / barajas_restantes
        if true_count > 1.0:
            return apu_hi
        elif true_count < -1.0:
            return apu_lo
        else:
            return apu_med

    def jugada(self, croupier, jugador):
        """ Indica la mejor opción dada la mano del croupier (que se supone que
            consta de una única carta) y la del jugador
        :param croupier: La carta del croupier
        :param jugador: La lista de cartas de la mano del jugador
        :return: La mejor opción: 'P' (pedir), 'D' (doblar), 'C' (cerrar) o 'S' (separar)
        """
        vc = croupier.valor
        vj = sum(c.valor for c in jugador)
        if len(jugador) == 2 and jugador[0].valor == jugador[1].valor:
            return Estrategia.MATD[vj//2 - 1][vc - 1]
        if any(c.valor == 1 for c in jugador) and vj < 12:
            return Estrategia.MATA[vj - 3][vc - 1]
        return Estrategia.MATN[vj - 4][vc - 1]

#========================================================================================

class Mazo(object):
    """ Clase que representa un mazo de cartas
    """
    NUM_BARAJAS = 2

    def __init__(self, clase_carta, estrategia):
        """ Crea un mazo y le asocia una estrategia
        :param clase_carta: La clase que representa las cartas
        :param estrategia: La estrategia asociada
        """
        self.clase = clase_carta
        self.estrategia = estrategia
        self.cartas = []
        random.seed()

    def reparte(self):
        """ Reparte una carta del mazo
        Llama al método cuenta_carta de la estrategia asociada
        :return: Un objeto carta de la clase indicada en el constructor
        """
        if len(self.cartas) == 0:
            # Se ha acabado el mazo: crear uno nuevo
            inds = list(range(52)) * Mazo.NUM_BARAJAS
            random.shuffle(inds)
            self.cartas = [self.clase(i) for i in inds]
        c = self.cartas.pop()
        if self.estrategia is not None:
            # Se informa a la estrategia de la carta que se reparte
            self.estrategia.cuenta_carta(c)
        return c
#========================================================================================    
class Mano(object):
    def __init__(self,nombre="Mano",apuesta=10):
        """ 
        cartas: lista que guarda las cartas
        estado: 0 abierta, 1 cerrada, 2 pasada
        """
        self.cartas=[]
        self.estado=0
        self.nombre=nombre
        self.apuesta=apuesta

    def anadir(self, carta):
        self.cartas.append(carta) 
        if self.valor>21:
            self.estado=2
        if self.valor==21:
            self.estado=1
            
    def separar(self):     
        # Crea dos objetos nuevos mano y establece las apuestas
        manoA = Mano(self.nombre + "A",self.apuesta)
        manoB = Mano(self.nombre + "B",self.apuesta)

        # Mueve las cartas a cada mano
        manoA.anadir(self.cartas[0])
        manoB.anadir(self.cartas[1])

        lista=[manoA,manoB]
        return lista

    def __str__(self):
        """
        devuelve el string con la representación deluxe
        """
        maximo=max(len(self.nombre)+1,len(self.strEstado()))
        nombre=self.nombre+":"
        while len(nombre)<maximo:
            nombre+=" "
        valor=" ("+str(self.valor)+")"
        while len(valor)<maximo:
            valor+=" "
        if self.nombre!="Croupier":apuesta=" "+str(self.apuesta)+"$"
        else: apuesta="    "
        while len(apuesta)<maximo:
            apuesta+=" "
        estado=self.strEstado()
        while len(estado)<maximo:
            estado+=" "
        
        string=nombre
        for x in range(len(self.cartas)):
            string+="╭───╮"
        string+="\n"+valor
        for x in self.cartas:
            if len(x.figura)==2: string=string+"│ "+x.figura+"│"  
            else:string=string+"│ "+x.figura+" │"
            
        string+="\n"+apuesta
        for x in self.cartas:
            string=string+"│ "+x.palo+" │"
        string+="\n"+estado
        for x in self.cartas:
            string=string+"╰───╯"
        

        return string
        
    @property
    def sePuedeSeparar(self):
        """True si se puede separar. False si no"""
        c=False
        if len(self.cartas)==2:
            if(self.cartas[0].valor==self.cartas[1].valor):
                c=True
        return c
    @property
    def valor(self):
        """devuelve el valor de la mano mas favorable (ases pueden ser 1 o 11)"""
        total=0
        nAs=0 # el valor total y el numero de ases
        hayAses=False
        for carta in self.cartas: # va sumando los valores faciales y cuando encuentra un as lo registra
            total += carta.valor
            if carta.valor == 1:
                nAs += 1
                hayAses=True
        while (total+10) <= 21 and nAs: # suma 10 por cada as sin pasarse (siempre que nAs != 0)
            total += 10
            nAs -= 1

        return total
    def strEstado(self):
        """devuelve el string del resultado"""
        if self.estado==0:
            return "Abierta"
        elif self.estado==1:
            return "Cerrada"
        else:
            return "PASADA"
#========================================================================================
def compruebaApuesta(apuesta, vJugador, vCroupier): 
    """comprueba en orden de prioridad quien gana"""
    if vJugador>21: # si el jugador se pasa siempre pierde
        r = -apuesta
    elif vCroupier>21: # si el croupier se pasa pero el jugador no, gana el jugador
        r = apuesta
    elif vJugador>vCroupier: # ninguno se pasa y el jugador tiene mas valor que el croupier, gana el jugador
        r =  apuesta
    elif vJugador<vCroupier: #ninguno se pasa y el croupier tiene mas valor que el jugador, pierde el jugador
        r = -apuesta
    else:   #la unica posibilidad restante es el empate, en tal caso devuelve 2
        r=0
    return r
#========================================================================================
class MyApp(wx.App):
    def OnInit(self):
        self.frame = MyFrame(None, wx.ID_ANY, "")
        self.SetTopWindow(self.frame)
        self.frame.Show()
        event = wx.CommandEvent(wx.EVT_TOGGLEBUTTON.typeId, self.frame.manualAuto.GetId())
        wx.PostEvent(self.frame.manualAuto, event)
        return True

# end of class MyApp

if __name__ == "__main__":
    app = MyApp(0)
    app.MainLoop()
