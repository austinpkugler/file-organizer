from tkinter import filedialog
from tkinter import messagebox
from tkinter import *
import datetime
import shutil
import os


class FileOrganizer:

    def __init__(self):
        self.canvas = Tk()
        self.width = 420
        self.height = 200
        self.path_input = Entry(self.canvas, width = 55)
        self.success_message = Text(self.canvas, width = 45, height = 1)
        self.path = ''
        
    def main(self):
        self.canvas.title("File Organizer for Windows")
        self.canvas.resizable(False, True)
        heading = Label(self.canvas, text = "File Organizer", font = ("Arial Bold", 20))
        heading.place(x = self.width * 0.5, y = self.height * 0.1, anchor = "center")

        self.path_input.place(x = self.width * 0.5, y = self.height * 0.3, anchor = "center")
        
        browse_btn = Button(self.canvas, height = 1, text = "...", command = self.browse)
        browse_btn.place(x = self.width * 0.95, y = self.height * 0.3, anchor = "center")
        
        organize_btn = Button(self.canvas, text = "Organize", command = self.organize)
        organize_btn.place(x = self.width * 0.5, y = self.height * 0.5, anchor = "center")

        self.success_message.place(x = self.width * 0.5, y = self.height * 0.7, anchor = "center")

        self.canvas.geometry(str(self.width) + 'x' + str(self.height))

        self.canvas.mainloop()

    def browse(self):
        self.path = filedialog.askdirectory()
        self.path_input.delete(0, "end")
        self.path_input.insert(0, self.path)

    def organize(self):
        duplicate_status = 'ignored '
        try:
            self.path_input.delete(0, "end")

            # Get the date modified of each file.
            path_tree = os.listdir(self.path)
            timestamps = []
            for i in path_tree:
                date_modified = os.path.getmtime(os.path.join(self.path, i)) # os.path.getctime will search for date created
                date_modified = datetime.datetime.utcfromtimestamp(date_modified).strftime("%Y/%m")
                date_modified = date_modified.replace("/", "-")
                timestamps.append(i + "||" + date_modified)

            # Create folders for each year and month the files were modified.
            folder_names = []
            for i in timestamps:
                i = ("".join(i)).split("||")
                folder_names.append(i[1])
            for i in folder_names:
                if os.path.exists(i) == False:
                    os.makedirs(os.path.join(i))
                    
            # Organize the files into their respective folders.
            saved_count = 0
            duplicate_count = 0
            for i in timestamps:
                date_modified = str(i[-7:])
                if date_modified in folder_names:
                    try:
                        shutil.move(self.path + "\\" + path_tree[timestamps.index(i)], date_modified)
                        saved_count += 1
                    except:
                        duplicate_count += 1

            # Delete the directory that the program was called on.
            folder_to_delete = self.path.split('/')
            print(folder_to_delete)
            folder_to_delete = str(folder_to_delete[len(folder_to_delete)-1])
            print(folder_to_delete)
            if (folder_to_delete not in folder_names):
                try:
                    os.rmdir(self.path)
                except:
                    confirm = messagebox.askquestion ('Warning!', 'There are duplicate files in "' + self.path + '." Are you sure you want to delete them?', icon = 'warning')
                    if confirm == 'yes':
                        duplicate_status = 'deleted '
                        shutil.rmtree(self.path)
                    else:
                        messagebox.showinfo('Success!', 'The directory at "' + self.path + '" has not been deleted.')
            else:
                messagebox.showerror("Process Failed!", "You cannot organize an already organized folder. All files will be ignored.")        

            # Output a message with the number of files moved and the number ignored.
            result = "Saved " + str(saved_count) + " files and " + duplicate_status + str(duplicate_count) + " duplicates."
            self.success_message.delete(0.0, "end")
            self.success_message.insert(1.0, result)
        except Exception as error:
            messagebox.showerror("Process Failed!", "Organization has failed with error: " + str(error))
        
organize = FileOrganizer()
organize.main()
    


