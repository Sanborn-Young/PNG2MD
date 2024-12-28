# PNG2MD
A small compiled Python Program To Convert a PNG into a MD file, which I built to help pull PNG files into files to Obsidian as text.

# GIVE IT TO ME NOW:

1. Click on the file that says PNG2MD.exe in the file list
2. Click on the github download icon, and put it anywhere you can double click on it.
3. Windows will warn you that it hasn't check it out, and if you are worried about it, you'll need to compile it yourself
4. Double click and it to run it.  It is barebones, so only one file.
5. If you don't plan to recompile the code, you don't need any other files

# A Longer Summary:  Who is this for?

_For markdown users that use PNG files in their Obsidian Vault (or other markdown packages) and want to quickly turn separate PNG files into text files that you can embed in any Obsidian (markdown) page so so that the image is carried along inside the text file_

**Details**

If you use Obsidian, any imported graphic PNG files are held in a directory by your note.md file.  The image is then hot linked into the note so you can see the image.  However, if you want to send the MD file somewhere, you have to also send the images as a separate image, or you need to compile the note into something like a PDF, which is not easily edited.  

The work around is to embedded the image in your note as an ASCII data string with the right wrapper.  [IBM docling will do this](https://github.com/DS4SD/docling), bit it embeds it as a PNG file, which is pretty big.  To make the image as small as possible, I use webp compression.  I then put the wrapper around the data, which is very small, and I save it as a .md file.  This means you can now open it.

When you put it in as a ASCII data string, it gets 33% larger due to ASCII only using 6 or 8 bits.  However, webp files are pretty small.

Why PNG files as the base?  The snipping tool in Win11 defaults to PNG, so I found that I was using PNG files a lot.

### 1. This is a compiled python script to run under Windows
- **Only tested to run under Win 11 Home and Pro**:  However, probably can run under Win 10.  Post results

### 2. No external modules required
- **This is self contain, which means it has no real options**: Just double click on the program.  If you don't like the compression level, you'll need to recompile the python code.

### 3. Uses the `webp` Python Library:
-  It is set to 1080 at quality level of 20.  For most text files this does a pretty good job of being readable, and is really small.

### 4. Compiling the Script with PyInstaller:
- **Updated the Spec File**: Modified the `PNG2MD.spec` file to include necessary imports and ensure all dependencies are bundled.  If you want to change something, you'll need to modify the python code and recompile it with the changes.  Alternatively, you could just run it as a python script, but you need all the dependencies rolled in.  Also, I used the UPX github to shrink the exe under github 25MB limit so you can just download the file.


### Most Non-Tech People:
- **Just download the executable**: When run, the program will bring up a GUI dialog box that will allow you to double click on any PNG file.  It will then turn the PNG into a .webp file and put it in the same directory with the same name.  It will then turn the .webp file into a .md file that you can read directly in a program like Obsidian or any other markdown editor.
- You have three versions of the same file, the original PNG, a compressed webp file, and finally a md file.  Delete any version you don't want.
- If you copy the .md file into your vault, you can open it with Obsidian.  Then you can use the merge function in Obsidian to merge it into any existing note, or have it as stand alone.
- If it shows up just as text place the cursor outside of the data stream or click the view option for the note rather than editing option.

### Sample Sizes For A Screenshot Original PNG, webp, and final .md file


| Screenshot 2024-12-27 210156.png  | 12/27/2024 21:02 | PNG File  | 37 KB |
|-----------------------------------|------------------|-----------|-------|
| Screenshot 2024-12-27 210156.webp | 12/27/2024 21:03 | Webp File | 10 KB |
| Screenshot 2024-12-27 210156.md   | 12/27/2024 21:03 | MD File   | 13 KB |


I hope this summary helps! If you have any more questions or need further assistance, feel free to ask. 😊
