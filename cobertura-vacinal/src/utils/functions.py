import os
import time
from utils.constants import DOWNLOAD_PATH


def save_file(name: str, year: str):
  files_before = set(os.listdir(DOWNLOAD_PATH))

  # Wait for download to start by detecting a new file
  temp_file_path = None
  final_file_path = None
  
  for _ in range(15): # wait up to 15 seconds for download to start
      files_after = set(os.listdir(DOWNLOAD_PATH))
      new_files = files_after - files_before
      # print("new files:", new_files)
      if new_files:
          filename = new_files.pop()
          path = os.path.join(DOWNLOAD_PATH, filename)
          if filename.endswith('.crdownload'):
              print("Download started, temporary file found.")
              temp_file_path = path
              break
          else:
              print("Download started and finished quickly.")
              final_file_path = path
              break
      time.sleep(2)

  if temp_file_path:
      # Now wait for the .crdownload file to be removed (i.e., download is complete)
      for _ in range(30): # wait up to 30 more seconds
          time.sleep(1)
          if not os.path.exists(temp_file_path):
              # Temp file is gone, so the real file should be there.
              final_filename = os.path.basename(temp_file_path).replace('.crdownload', '')
              path = os.path.join(DOWNLOAD_PATH, final_filename)
              # It can take a moment for the final file to be available
              for __ in range(5):
                if os.path.exists(path):
                    print("Download completed.")
                    final_file_path = path
                    break
                time.sleep(1)
              if final_file_path:
                break
  
  if final_file_path:
      downloaded_filename = os.path.basename(final_file_path)
      
      # Sanitize name for filename
      sanitized_name = "".join(c for c in name if c.isalnum() or c in (' ', '-')).rstrip().replace(' ', '_')
      new_filename = f"{year}-{sanitized_name}.xlsx"
      new_filepath = os.path.join(DOWNLOAD_PATH, new_filename)

      # Ensure the old file exists before trying to rename
      if os.path.exists(final_file_path):
        
          # If a file with the new name already exists, remove it
          if os.path.exists(new_filepath):
              os.remove(new_filepath)
          os.rename(final_file_path, new_filepath)
          print(f"Renamed '{downloaded_filename}' to '{new_filename}'")
      else:
          print(f"Error: Downloaded file '{downloaded_filename}' not found.")
  else:
      print(f"Download did not start or complete in time for vaccine: {name}")
