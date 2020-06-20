import os
def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.
    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.
    There are no limit to the depth of the subdirectories can be.
    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system
    Returns:
       a list of paths
    """

    list_of_paths = []
    for item in os.listdir(path):
      # print(os.path.join(path, item))
      if os.path.isfile(os.path.join(path, item)): 
        if item.endswith(suffix):
          list_of_paths.append(os.path.join(path, item))
        
      else:
        list_of_paths.extend(find_files(suffix, os.path.join(path, item)))
    
    return list_of_paths
    

result = find_files('.c', 'testdir')
print(result)
