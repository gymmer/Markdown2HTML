## run.py

This program is main to **transform MarkDown to HTML**.  
MarkDown is `.md` file, and HTML is `.txt` file.  

To start, you can:  
  
>  1. Put `.md` files into the `input` folder.   
    What's more, you can put multiple files.
>  2. Open the python shell, the run the command:  
        `python run.py`
>  3. Then, you can find the .txt files in the `output` folder.  
    The `.html` file-name is the same as `.md`.

This program only supports **English** MarkDown file-name,  
but suppots **both English and Chinese** MarkDown file-content.

The core algorithm is Sublime Text plugin, **Markdown Preview**,
which can be get from https://github.com/revolunet/sublimetext-markdown-preview

---

## empty_output.py

This program is main to **empty the output folder**.  
Only the files in it will be deleted.  
The folder will still exist.

To start, you can:
  
> Open the python shell, the run the command:  
        `python empty_output.py`

---

***Enjoy yourself!***