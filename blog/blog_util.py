import os, glob, sys
import shutil

__project_dir__ = None

def get_current_dir():
    return os.path.dirname(os.path.realpath(__file__))

def get_md_path():
    path = sys.argv[1]
    if not sys.argv[1].endswith("/"):
        path = sys.argv[1] + "/"
    #print("debug in get_md_path:" + path)
    return path


def get_html_path():
    md_path = get_md_path()
    return md_path.replace("md", "html")

# make sure we follow this protocol
def get_image_path():
    md_path = get_md_path()
    return md_path.replace("md", "images")

def check_html_directory():
    html_path = str(get_html_path())
    if not os.path.exists(html_path):
        print(str(html_path) + " directory not exists, do you want to create it? Y/N")
        answer= str(input())
        if answer.lower() == 'y':
            try:
                os.mkdir(html_path)
            except Exception as e:
                parent_dir = os.path.dirname(html_path)
                if not os.path.exists(parent_dir):
                    raise Exception(parent_dir+ " directory not exists, please create it before")
            print("dir created successfully!")
        else:
          raise Exception(html_path + " directory not exists, please create it before")
    else:
        html_files=os.listdir(html_path)
        # if dir exists and html exist, delete them and regenerate
        if (len(html_files)>0):
             for file in html_files:
                if file.endswith(".html"):
                    os.remove(os.path.join(html_path, file))
       

def get_all_markdown_files(input_dir):
    md_files=list()
    for file in os.listdir(input_dir):
        if file.endswith(".md"):
            #mdFiles.append(os.path.join(inputDir, file))
            md_files.append(file)
            #print(os.path.join(inputDir, file))
    print(md_files)
    return md_files

def create_html_files(md_files):
    html_files = []
    for mdFile in md_files:
        html_file = os.path.join(get_html_path(), str(mdFile).replace(".md",".html"))
        # keep this logging
        print("creating the html file:")
        html_files.append(html_file)
        print(html_file)
        shutil.copyfile("html/template.html", html_file)

        # replace string .md file in the html file
        with open(html_file, "r") as f:
            dir_depth = html_file.count("/")

            relative_md_file_path = '../' * dir_depth + get_md_path() + mdFile
            print("replacing template md file in the html source using the following path.")
            print(relative_md_file_path)
            new_text = f.read().replace("../md/file.md", relative_md_file_path)
        with open(html_file, 'w') as f:
            f.write(new_text)
    return html_files

def generate_blog_links(urls):
   title_li_start = "<li><span class=\"caret\">"  +sys.argv[1] + "</span>"
   nested_ul_start = "  <ul class=\"nested\">"
   inner_li_entry = ""
   count = 0
   for url in urls:
     link_name = url.split("/")[-1].replace("_"," ").replace(".html"," ").strip()
     print(link_name)
     inner_li_entry += "    <li><a href=\"blog/" + url + "\">{}</a></li>".format(link_name)
     if count!=len(urls)-1:
         inner_li_entry += "\n"
     count +=1

   nested_ul_end = "  </ul>"
   title_li_end = "</li>"
   html_section = title_li_start + "\n" + nested_ul_start + "\n" + inner_li_entry + "\n" + nested_ul_end + "\n" + title_li_end
   print(html_section)
   return html_section


# Normally we would move images to images/folder and we follow the same directory structures.
# Just in case that files in the /html folders would be deleted.
# This moving code is ok but just in case,

def mv_image_files():
    os.chdir(get_md_path())
    types = ('*.png', '*.jpg') # the tuple of file types
    files_grabbed = []
    for files in types:
        files_grabbed.extend(glob.glob(files))
    print(files_grabbed)

    for imgFile in files_grabbed:
        target_image_file = os.path.join(get_current_dir(),get_image_path(), imgFile)
        src_img_file = os.path.join(get_current_dir(),get_md_path(), imgFile)
        # keep this logging
        print("======================")
        print(src_img_file)
        print(target_image_file)
        print()
        shutil.move(src_img_file, target_image_file)