# DictionaryVisualization
Visualization of Dictionary data structure 


## Program Description
- The program runs a GUI visualization for the user, and illustrates the operation principle of the Dictionary data structure while implementing its commands.
- The dictionary will be displayed at the bottom of the screen with all the keys and values arranged in a table with their index, hash value, and status number of each     cell:
  - Occupied
  - Free
  - Deleted
- The user can enter new entries in the dictionary with the insert button, delete entries from the dictionary with a button (delete if the entry is in the dictionary).
- The get button will display the value for the inserted key.
- The index button will return the index where the inserted key is located.
- The clear button will clear the entire table.
- The keys button will display all the keys in the table.
- The values button will display all the values in the table.
- The items button will display all the key, value pairs in the table.
- In addition there are 4 radio buttons for selecting the collision handling function:
  - Linear
  - Quadratic
  - Double Hashing
  - Custom
 - And a message window in the center of the screen for displaying user outputs.
 
 
 
 ## Operating Instructions
 **Run the MainApp.py file to run the application.**
 1. First select the Collision Function handling by marking the desired radio button, from the moment the button is selected the program will lock the selected               function and will update the dictionary.
 2. Switching between the radio buttons will show the equation of the Collision Function respectively.
 3. Changing the collision handling function is only possible at the beginning of each program or after clearing the dictionary using the Clear button.
 4. From now on, you can enter values in the dictionary using the Key and Value windows.
 5. For Insert operation:
    - It is necessary to enter a Key and Value (the interface will illustrate the insertion to the table).
    - Any input consisting of numbers only will be counted as a number.
    - Any other input that consists of a combination of numbers and letters or characters will be counted as a string.
    - A string can be inserted with the addition of "" and without.
    - If you want to insert blank input, you can do so using blank "" or ""
6. For Get action:
   - You need to enter a Key that you want to look for in the table.
   - Given a Key that exists in the table, its value will return to the Value window.
   - Given a Key that does not exist, an error message will be returned.
7. For Delete operation:
   - You need to enter a Key that you want to delete.
   - If it exists in the table, both the key and the value will be deleted.
   - After deleting, a <Dummy> mark will be marked in the table, which symbolizes a deleted area that cannot be stored until the dictionary grows (resize).
8. For Index operation:
   - You need to enter a Key that you want to get its index in the table.
   - If the Key doesn't exist an error message will pop up.
9. For Keys operation:
   - All dictionary keys will be printed in the Output Window.
10. For Operation Values:
    - All dictionary values will be printed in the Output Window.
11. For Action Items:
    - All dictionary items {key: value} will be printed in the Output Window.
12. For Clear operation:
    - All dictionary items will be deleted.
    - All settings will be initialized.
    - The table will be cleaned and reset.
    - The selection of collision handling functions will be re-enabled.
13. For any attempt of an illegal action an error message will pop up describing the error.
  
  
  
  ## GUI
  ![image](https://user-images.githubusercontent.com/108329249/177845056-8ac97643-3f60-476c-9e74-b561e298a750.png)

  ![image](https://user-images.githubusercontent.com/108329249/177845075-7ddee9d4-c102-40db-b813-1b2578e14f24.png)

 
 
