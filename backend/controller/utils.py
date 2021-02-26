import os
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename


def upload_file(the_file):

        if the_file :
            filename = secure_filename(the_file.filename)
            print(filename)
            the_file.save(os.path.join('backend/upload_files/', filename))
            return 'backend/upload_files/'+filename
        return None