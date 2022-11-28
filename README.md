# Budget App

This is a project represenging an app for logging expenses and budgeting. The program maintains multiple ledgers of expenses for different categories of spending.

Each category represents a type of expense. An example of the output for a `Food` category would look like:

    *************Food*************
    initial deposit        1000.00
    groceries               -10.15
    restaurant and more foo -15.89
    Transfer to Clothing    -50.00
    Total: 923.96

 The user can depost funds into each category, withdraw funds from them, or even transfer money between different categories.

 Additionally, the program also prints a graph of the percentage spent on each category. A sample output of three categories, such as `Food`, `Clothing`, and `Auto`,  would look like:

    Percentage spent by category
    100|          
     90|          
     80|          
     70|          
     60| o        
     50| o        
     40| o        
     30| o        
     20| o  o     
     10| o  o  o  
      0| o  o  o  
        ----------
        F  C  A  
        o  l  u  
        o  o  t  
        d  t  o  
           h     
           i     
           n     
           g     

Additional details for the project can be found [here](https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/budget-app).
