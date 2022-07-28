# The Page object is u

## Acknowledgments
1. [Iakiv Kramarenko](https://github.com/yashaka)
## About HomeWork
### Основное задание
1. Применение инструментов **Модульной Парадигмы**
   1. Вынести в отдельный модуль функцию-хелпер для трансформации пути к файлу с
   относительного в абсолютный, реализовав эту функцию, если это еще не сделано.
2. Применение инструментов Объектно-Ориентированной Парадигмы
   1. Повторить показанное в уроке, создав PageObject для контрола типа 
   «Tags Input». Добавить в "шаблон фабрики" 
   оба способа работы с контролом – через автодополнение по Tab и 
   выбор из списка предложенных вариантов.
   2. Реализовать PageObject для контрола «Dropdown с автодополнением», 
   с возможностью устанавливать значение для поля как через автодополнение 
   по Tab, так и выбор из списка.
   3. Реализовать PageObject для контрола DatePicker с возможностью как
   установить значение в поле ввода явно, так и выбрать нужную дату 
   из диалога дейтпикера.
   4. Реализовать PageObject для контрола «Table», использующийся в тесте 
   для проверки результата подтверждения формы.

Бонусное задание (сдавать в отдельной бренче)

1.2* Вместо PageObject реализовать в отдельном модуле функцию для работы 
с контролом «Tags Input», которая в зависимости от переданных именованых 
аргументов будет либо автодополнять введенный текст по Tab, либо выбирать 
по клику из предложенных в списке.


## Steps
1. Refactoring the code #1.
   1. The select control of `state and city`.
   2. The check-box control of `hobbies`.
   
      Added the selection of all hobbies by using the selector .
      and the exact hobby name.
   3. The subjects container of `Subjects`.
   
      Added the two ways of selections of subjects: press_enter() and click().
   4. The drop-down control for `City`.
      Changed the way of typing value. Used the function `type()`.
   5. Updated the check of the field `Student Name`. 
      1. Used the multi-checking fields (label, value) in the row `Student Name`.
      2. DRY: getting a row by index.
         Created the function `cells_of_row`.
   6. Created the helpers
      1. Get the path to a file in the resources.
      2. Created the custom command `upload_resourc` for uploading a file.
         
         E.g. 
         ```
         browser.element("#uploadPicture")
                .perform(upload_resource('requirements.txt'))
         ```
   7. Created a help function `get_texts_from_row` 
      for getting texts from a row of the result table.
      
      **Using**
      `assert get_texts_from_row(9) == f'{"State and City"} {"NCR Delhi"}'`
2. Refactoring the code #2.
   1. Removed the selector `tbody` from the result table selector.
   2. Helpers 
      1. Created the function select `State and City`.
      2. Created the function select `Subjects`.
3. HomeWork #6
   1. Created the file helper.py (see 1.6) 
   2. PageObject
      1. Created class TagsInput for the "Subject" element. 
         Added two methods: add and autocomplete.
      2. Created class DropDown for the elements 'State and City'. 
      3. Created class Calendar for the element 'Date of Birth'.
      4. Created class Table. Maked the chain for the methods.  
     

Бонусное задание (сдавать в отдельной бренче)

1.2* Вместо PageObject реализовать в отдельном модуле функцию для работы 
с контролом «Tags Input», которая в зависимости от переданных именованых 
аргументов будет либо автодополнять введенный текст по Tab, либо выбирать 
по клику из предложенных в списке.

## What's new
1. How click on a hidden button
   1. Use `perform` like this
   `perfomn("command.js.click")`
   2. Use `with`
   `with_(click_by_js = True).click()`

   **Notice** that this way is used for many clicks. 
2. How fill a field
   1. Use `type()` or `set_value()`
   
   **Note.** The chain of functions `clear().type()` is similar to  `set_value()`.
3. Added the waiting for all selene actions
   
   Set in the config this `browser.config.wait_for_no_overlap_found_by_js = True`.
   
   **Notice** that in selene only `click()` wait for a usable element.
4. After the program finishes the browser window is not closed.  
   `browser.config.hold_browser_open = True`


## Resources

## Miscellaneous


