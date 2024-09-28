import click
import os
import bibtexparser
from .utils import load_template_file


@click.group()
def lit_rev():
    pass


@lit_rev.command()
@click.option('-k','--bibtex-key')
@click.option('-p','--prompt-for-filename',is_flag =True)
@click.option('-f','--file-name', help='file name to write out')
@click.option('-o','--out_path',default= '.',
              help='directory to save the file')
@click.option('-t','--template_name', default ='paper',
              help='file name of template or local path')
@click.option('-l','--local-template',is_flag =True)

def new(bibtex_key,prompt_for_filename,file_name ,
        out_path,template_name,local_template):
    '''
    start a new file, use key if provided or prompt
    '''

    if not(bibtex_key):
        bibtex_key = click.prompt('what is the bibtex key of the paper you will summarize',type=str)

    if prompt_for_filename:
        file_name = click.prompt('what file name would you like to use (no extension)',type=str)

    # use key if not provided either format
    if not(file_name):
        file_name = bibtex_key.lower() + '.md'

    if local_template:
        #  read from local file
        with open(template_name,'r') as f:
            template = f.read()
    else:
        # add extension and load
        template_name += '.md'
        template = load_template_file(template_name)

    

    # picks first if multiple
    bibtex_file = [file for file in os.listdir() if '.bib' in file][0]
    # TODO: make it acutally append multiple together before parsing
    # bib_files = '\n'.join([bib for bib in ])
    with open (bibtex_file,'r') as f:
        bibtex_str = f.read()

    library =  bibtexparser.parse_string(bibtex_str)
    # keep first match
    target_entry = [entry for entry in library.entries if entry.key == bibtex_key][0]

    target_info = {key:feild.value for  key,feild in target_entry.fields_dict.items()}


    filled_template = template.format(bibtex_key= bibtex_key,**target_info)

    file_out = os.path.join(out_path,file_name)
    with open(file_out,'w') as f:
        f.write(filled_template)