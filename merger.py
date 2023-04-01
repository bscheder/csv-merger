from tkinter import *
from tkinter import messagebox,filedialog,Entry

# ---------------------------- CONSTANTS ------------------------------- #
YELLOW = "#f7f5dd"
GREEN = "#9bdeac"
FONT_NAME = "Courier"
MAX_LENGTH = 0 #TODO depricated , kill it
FILE_PATH = None #TODO depricated , kill it
OUTPUT_PATH = None 
CSCS_PATH = None
DOMAIN_COLUMN = None
DR_COLUMN = None 
CONTACTES_SITES = None


# ---------------------------- DIVIDE MECHANISM ------------------------------- # 
def write_to_file(filename,rows):
    with open(OUTPUT_PATH + '/' + filename,'w+') as file:
        for row in rows:
            file.write(row)

def merge():
    global MAX_LENGTH
    
    if CSCS_PATH is None:
        messagebox.showerror(title='Error', message='Please add the path of csv\'s folder!')
    elif DOMAIN_COLUMN is None:
        messagebox.showerror(title='Error', message='Please add the name of the domain column!')
    elif DR_COLUMN is None:
        messagebox.showerror(title='Error', message='Please add the name of the DR column!')
    elif CONTACTES_SITES is None:
        messagebox.showerror(title='Error', message='Please add the path of the contactes site\'s table!')
    elif OUTPUT_PATH is None:
        messagebox.showerror(title='Error', message='Please add a the output path of merged table!')

   



def select_dir():
    global CSCS_PATH
    dir = filedialog.askdirectory()
    cvs_dir_path.insert(0, dir)
    CSCS_PATH = dir   

def set_contacted_site():
    global CONTACTES_SITES
    f_types = [('Tables', '*.xlsx *.csv')]
    filename = filedialog.askopenfile(filetypes=f_types)
    contacted_sites.insert(0, filename.name)
    CONTACTES_SITES = filename.name     

def set_output_path():
    global OUTPUT_PATH
    dir = filedialog.askdirectory()
    output_path.insert(0, dir)
    OUTPUT_PATH = dir

def select_domain_header():
    global DOMAIN_COLUMN
    value = domain_header.get()
    try:
        DOMAIN_COLUMN = str(value)

        if DOMAIN_COLUMN == '':
            messagebox.showerror(title='Error', message='Please add the name of the domain header!')    

    except ValueError:
        messagebox.showerror(title='Error', message='Please add the name of the domain header!')

def select_dr_header():
    global DR_COLUMN
    value = domain_header.get()
    try:
        DR_COLUMN = str(value)

        if DR_COLUMN == '':
            messagebox.showerror(title='Error', message='Please add the name of the DR header!')    

    except ValueError:
        messagebox.showerror(title='Error', message='Please add the name of the DR header!')

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Csv Merger")
window.config(padx=100, pady=50, bg=GREEN)
window.resizable(0,0)

title_label = Label(text="CSV Merger", fg=YELLOW, bg=GREEN, font=(FONT_NAME, 50))
title_label.grid(column=1, row=0)

csv_dir_label = Label(text="Csvs Path:",bg=GREEN, font=(FONT_NAME, 18))
csv_dir_label.grid(column=0, row=1)

cvs_dir_path = Entry(window,width=50)
cvs_dir_path.grid(column=1, row=1)

cvs_dir_browse = Button(text="Browse", highlightthickness=0,command=select_dir)
cvs_dir_browse.grid(column=2, row=1)

domain_header_label = Label(text="Domain Header:",bg=GREEN, font=(FONT_NAME, 18))
domain_header_label.grid(column=0, row=2)

domain_header = Entry(window,width=50)
domain_header.grid(column=1, row=2)

dh_browse = Button(text="Submit", highlightthickness=0,command=select_domain_header)
dh_browse.grid(column=2, row=2)

dr_header_label = Label(text="DR Header:",bg=GREEN, font=(FONT_NAME, 18))
dr_header_label.grid(column=0, row=3)

dr_header = Entry(window,width=50)
dr_header.grid(column=1, row=3)

drh_browse = Button(text="Submit", highlightthickness=0,command=select_dr_header)
drh_browse.grid(column=2, row=3)

contacted_sites_label = Label(text="Contacted Sites:",bg=GREEN, font=(FONT_NAME, 18))
contacted_sites_label.grid(column=0, row=4)

contacted_sites = Entry(window,width=50)
contacted_sites.grid(column=1, row=4)

csites_save = Button(text="Browse", highlightthickness=0,command=set_contacted_site)
csites_save.grid(column=2, row=4)

output_label = Label(text="Output:",bg=GREEN, font=(FONT_NAME, 18))
output_label.grid(column=0, row=5)

output_path = Entry(window,width=50)
output_path.grid(column=1, row=5)

output_browse = Button(text="Browse", highlightthickness=0,command=set_output_path)
output_browse.grid(column=2, row=5)

divide_button = Button(text="Get my list!", highlightthickness=0, command=merge)
divide_button.grid(column=1, row=6)

window.mainloop()
