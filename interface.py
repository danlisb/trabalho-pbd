from tkinter import *
import os
from pygame import mixer
import PIL
import stagger
from tkinter import ttk
from PIL import ImageTk
import io
from tkinter.filedialog import askdirectory
from pathlib import Path

# abre o diretório com as músicas
def fileopen():
    global st
    path = ""
    try:
        path = askdirectory(parent=root, title='Escolha a pasta com as músicas: ')
        if path == "":
            pass
        else:
            st = path
            playlist.delete(0, 'end')
            musiclist()
    except:
        pass

# modificar volume
def vol():
    if scale1.winfo_manager():
        scale1.place_forget()
    else:
        scale1.place(x=110, y=320)

def volume(val):
    global currentdir
    global st
    global vol1
    global img1
    os.chdir(currentdir)
    val1 = float(val)/100
    mixer.music.set_volume(val1)
    if (val1 == 0.0):
        volbutton['image'] = img1
    else:
        volbutton['image'] = vol1
    os.chdir(st)

# busca as músicas no diretório
def musiclist():
    global st
    os.chdir(st)
    songtracks = os.listdir()

    # insere as músicas na playlist
    for track in songtracks:
        if track.endswith(".mp3"):
            playlist.insert(END, track)
        else:
            pass

# mostra a imagem da música
def musicpic():
    global currentdir
    global st
    global photo
    global new_path
    try:
        mp3 = stagger.read_tag(new_path)
        by_data = mp3[stagger.id3.APIC][0].data
        im = io.BytesIO(by_data)
        imageFile = PIL.Image.open(im)
        imageFile = imageFile.resize((260, 300), PIL.Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(imageFile)
        label1.image = photo
        label1['image'] = photo
    except:
        os.chdir(currentdir)
        photo = PhotoImage(file="Music-Heart-icon.png")
        label1['image'] = photo
        os.chdir(st)

# tocar a música
def playmusic():
    global st
    global index
    global new_path
    global song_
    status.set("tocando")
    song_ = playlist.get(ACTIVE)
    new_path = os.path.join(st, song_)
    song.set(song_)
    mixer.music.load(song_)
    mixer.music.play()

    x = playlist.curselection()
    y = ()
    if (x == y):
        x = (0,)
    index = x[0]
    playbutton.place_forget()
    pausebutton.place(x=110, y=15)
    musicpic()

# pausar a música
def mscPause():
    status.set("Pausado")
    mixer.music.pause()
    pausebutton.place_forget()
    playbutton.place(x=110, y=15)

# tocar a próxima música
def mscProxima():
    global index
    global new_path
    playlist.activate(index+1)
    song.set(playlist.get(ACTIVE))
    song_ = playlist.get(ACTIVE)
    new_path = os.path.join(st, song_)
    mixer.music.load(playlist.get(ACTIVE))
    mixer.music.play()
    index = index+1
    musicpic()
    playbutton.place_forget()
    pausebutton.place(x=110, y=15)

# tocar a música anterior
def mscAnterior():
    global index
    global new_path
    playlist.activate(index-1)
    song.set(playlist.get(ACTIVE))
    song_ = playlist.get(ACTIVE)
    new_path = os.path.join(st, song_)
    mixer.music.load(playlist.get(ACTIVE))
    mixer.music.play()
    index = index-1
    musicpic()
    playbutton.place_forget()
    pausebutton.place(x=110, y=15)

# esconde a lista de músicas
def hide():
    if frame1.winfo_manager():
        frame1.place_forget()
        root.geometry("600x500")
        queuebutton['image'] = arrow2
    else:
        frame1.place(x=600, y=0, width=400, height=500)
        root.geometry("1000x500")
        queuebutton['image'] = arrow1

# main function
if __name__ == "__main__":
    root = Tk()
    photo = PhotoImage(file="images/fini.png")
    root.title("FiniMusic")
    root.geometry("600x520")
    root.iconbitmap('images/fini.ico')
    root.resizable(0, 0)
    root.configure(background="black")

    mixer.init()

    # imagens dos botões
    play = PhotoImage(file="images/Play.png")
    pause = PhotoImage(file="images/Pause.png")
    back = PhotoImage(file="images/backward.png")
    forward = PhotoImage(file="images/Forward.png")
    queuep = PhotoImage(file="images/interface.png")
    arrow1 = PhotoImage(file="images/arrows(1).png")
    arrow2 = PhotoImage(file="images/arrows.png")
    vol1 = PhotoImage(file="images/vol.png")
    img1 = PhotoImage(file="images/mute1.png")

    # inicializando variáveis
    song = StringVar()
    song.set("Bem vindo ao FiniMusic")
    status = StringVar()
    index = 0
    st = str(os.path.join(Path.home(), "Music"))
    currentdir = os.path.abspath(os.getcwd())
    new_path = ""

    # criando menu
    Menu1 = Menu(root)
    root.config(menu=Menu1)

    filemenu = Menu(root, tearoff=0)
    filemenu.add_command(label="Open", command=fileopen)

    Menu1.add_cascade(label="File", menu=filemenu)

    # criando frames
    musicframe = LabelFrame(root, bg="black", relief=GROOVE)
    musicframe.place(x=160, y=50, width=260, height=300)

    buttonframe = LabelFrame(root, bg="black", bd=0, relief=GROOVE)
    buttonframe.place(x=160, y=400, width=600, height=80)

    frame1 = LabelFrame(root, bg="black", relief=GROOVE)
    frame1.place(x=600, y=0, width=400, height=500)

    label1 = Label(musicframe, bg="black", image=photo, bd=0, relief=GROOVE)
    label1.pack(expand=True, fill=BOTH)

    label2 = Label(root, text="Bem vindo Ao FiniMusic", textvariable=song, bg="white", font=("times new roman", 16), fg="black", bd=0, relief=GROOVE)
    label2.pack(side=BOTTOM, fill=BOTH)

    # criando a playlist

    playlist = Listbox(frame1, selectbackground="gold", selectmode=SINGLE, font=("times new roman", 12, "bold"), bg="black", fg="red", bd=5, relief=GROOVE)
    playlist.pack(expand=True, fill=BOTH)

    musiclist()

    playbutton = Button(buttonframe, image=play, bg="black", bd=0, relief=GROOVE, command=lambda: playmusic())
    playbutton.place(x=110, y=15)

    pausebutton = Button(buttonframe, image=pause, bg="black", bd=0, relief=GROOVE, command=mscPause)

    queuebutton = Button(buttonframe, image=queuep,bg="black", bd=1, relief=GROOVE, command=hide)
    queuebutton.place(x=400, y=15)

    backbutton = Button(buttonframe, image=back, bg="black", bd=0, relief=GROOVE, command=mscAnterior)
    backbutton.place(x=0, y=15)

    forwardbutton = Button(buttonframe, image=forward, bg="black", bd=0, relief=GROOVE, command=mscProxima)
    forwardbutton.place(x=215, y=15)

    volbutton = Button(root, image=vol1, bg="black", activebackground="white", bd=0, relief=GROOVE, command=vol)
    volbutton.place(x=100, y=425)

    scale1 = ttk.Scale(root, from_=100, to=0, orient=VERTICAL, command_=volume)

    root.mainloop()
