# PNG2MD
A small compiled Python Program To Convert a PNG into a MD file, which I built to help pull into files to Obsidian.

# GIVE IT TO ME NOW:

1. Click on the file that says PNG2MD.exe
2. Click on the download icon, and put it anywhere you can double click on it.
3. Windows will warn you that it hasn't check it out, and if you are worried about it, you'll need to compile it yourself
4. Double click and it and pick your file

# A Longer Summary:  Who is this for?

_For markdown users that use PNG files in their Obsidian Vault (or other markdown packages) and want to quickly turn separate PNG files into text files that you can embed in any Obsidian (markdown) page so so that the image is carried along inside the text file_

**Details**

If you use Obsidian, any imported graphic PNG files are held in a directory by your note.md file.  The image is then hot linked into the note so you can see the image.  However, if you want to send the MD file somewhere, you have to also send the images as a separate image, or you need to compile the note into something like a PDF, which is not easily edited.  

The work around is to embedded the image in your note as a data string.  IBM docling will do this, and it embeds it as a PNG file.

If you use Win11, the snipping tool defaults to PNG images, which I find as a very standard package.

However, PNG files are not the most space efficient.  So this tool turns any PNG into a webp file, and wraps a header on it so you can simply open it in Obsidian (or other similar packages).



### 1. This is a compiled python script to run under Windows
- **Only tested to run under Win 11 Home and Pro**:  However, probably can run under Win 10.  Post results

### 2. No external modules required
- **This is self contain, which means it has no real options**: Just double click on the program

### 3. Uses the `webp` Python Library:
-  It is set to 1080 at quality level of 20.  For most text files this does a pretty good job of being readable, and is really small.

### 4. Compiling the Script with PyInstaller:
- **Updated the Spec File**: Modified the `PNG2MD.spec` file to include necessary imports and ensure all dependencies are bundled.  If you want to change something, you'll need to modify the python code and recompile it with the changes.  Alternatively, you could just run it as a python script, but you need all the dependencies rolled in.


### Most Non-Tech People:
- **Just download the executable**: When run, the program will bring up a GUI dialog box that will allow you to double click on any PNG file.  It will then turn the PNG into a .webp file and put it in the same directory with the same name.  It will then turn the .webp file into a .md file that you can read directly in a program like Obsidian or any other markdown editor.
- You have three versions of the same file, the original PNG, a compressed webp file, and finally a md file.  Delete any version you don't want.
- If you copy the .md file into your vault, you can open it with Obsidian.  Then you can use the merge function in Obsidian to merge it into any existing note, or have it as stand alone.
- If it shows up just as text place the cursor outside of the data stream or click the view option for the note rather than editing option.

I hope this summary helps! If you have any more questions or need further assistance, feel free to ask. 😊
