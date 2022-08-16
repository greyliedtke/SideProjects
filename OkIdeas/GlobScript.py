"""
Script to get all files in directory and create excel workbooks to manage...
"""

# import statements
import glob
import os
import time
import pandas as pd


# directory path
dire = os.getcwd()
dir_path = dire

# initialize columns
file_names = []
file_paths = []
file_mod_times = []
file_types = []
file_comments = []


# excel output file
excel_name = "Directory_Sheet.xlsx"
excel_path = dire+"\\"+excel_name
out_exists = os.path.exists(excel_path)

# running the script
# input('Press ENTER to run')


# function to walk through directory
def walk_through(directory, df=None):

    # looping for walking through system...
    for dirpath, dirs, files in os.walk(directory):

        for filename in files:

            fname = os.path.join(dirpath, filename)
            if 'virtual_env' in fname:
                # print('skip')
                continue

            mod_time = time.ctime(os.path.getmtime(fname))

            # checking if file is new
            if df is not None:
                # if path already exists, skip this row...
                if fname in df['File_Paths'].values:
                    continue

            # including file type if specified
            try:
                f_type = filename.split('.')[1]
                filename = filename.split('.')[0]
            except:
                f_type = 'NA'

            # adding to arrays
            file_names.append(filename)
            file_paths.append(fname)
            file_mod_times.append(mod_time)
            file_types.append(f_type)
            file_comments.append('')

    # creating the dataframe
    new_file_df = pd.DataFrame({
        'File_Names': file_names,
        'File_types': file_types,
        'File_Paths': file_paths,
        'File_mod_times': file_mod_times,
        'File_comments': file_comments
    })

    return new_file_df


def new_walk(directory, df_existing=None):

    # create dataframe of files in directory
    for dirpath, dirs, files in os.walk(directory):

        for filename in files:

            fname = os.path.join(dirpath, filename)

            # files to skip...
            if 'virtual_env' in fname:
                # print('skip')
                continue

            mod_time = time.ctime(os.path.getmtime(fname))

            # including file type if specified
            try:
                f_type = filename.split('.')[1]
                filename = filename.split('.')[0]
            except:
                f_type = 'NA'

            # adding to arrays
            file_names.append(filename)
            file_paths.append(fname)
            file_mod_times.append(mod_time)
            file_types.append(f_type)
            file_comments.append('')

    # creating the dataframe
    df_new = pd.DataFrame({
        'File_Names': file_names,
        'File_types': file_types,
        'File_Paths': file_paths,
        'File_mod_times': file_mod_times,
        'File_comments': file_comments
    })
    df_new.index.name = 'Index'

    if df_existing is not None:
        # df_existing.sort_values(by=['File_Names'])
        # df_new.sort_values(by=['File_Names'])
        df_existing.reset_index(drop=True)
        df_new.reset_index(drop=True)
        # df_existing.drop('Index', axis=1)
        # df_new.drop('Index', axis=1)
        df_existing.to_csv('existing_df.csv')
        df_new.to_csv('current_df.csv')
        # df_all = df_existing.merge(df_new, on='File_Names')
        # df_all.to_csv('df_all.csv')

        ds1 = set([tuple(values) for values in df_existing.values.tolist()])
        ds2 = set([tuple(values) for values in df_new.values.tolist()])

        ds1.symmetric_difference(ds2)
        # print(df1, '\n\n')
        # print(df2, '\n\n')

        print(pd.DataFrame(list(ds1.difference(ds2))), '\n\n')
        print(pd.DataFrame(list(ds2.difference(ds1))), '\n\n')

    df_new = 0
    df_old = 0

    return df_new, df_old
    # compare prev to current df...
    # new df of new files
    # new df of deleted files


# if file already exists
if out_exists:
    struct_df = pd.read_excel(excel_path, index_col='Index')
    # new_files_df, old_files_df = new_walk(dir_path, df_existing=struct_df)
    new_files_df = walk_through(dir_path, df=struct_df)

    # if there are new files... create a dataframe for such
    new_file_number = len(new_files_df.index)
    if new_file_number > 0:
        print(f"{new_file_number} new files")
        new_files_df.to_excel("new_files.xlsx")

    # otherwise say there are no new files
    else:
        print('no new files')

# creating a file

else:
    new_files_df = walk_through(dir_path)
    new_files_df.index.name = 'Index'
    new_file_number = len(new_files_df.index)
    print(f"{new_file_number} files in dir")
    new_files_df.to_excel(excel_name)
    new_files_df.to_excel(excel_name)


# exiting the script
input('Press ENTER to exit')


# end of script
