def func():
    global h_id_label
    global h_passw_label
    global h_email_label
    global h_name_label
    global h_type_label
    top = Toplevel()
    top.title('Sign Up For Asset Manager')

    donn = sqlite3.connect('assetmanage.db')
    d = donn.cursor()

    # submit button fuction
    def submit():
        conn = sqlite3.connect('assetmanage.db')
        d = conn.cursor()

        # INSERT VALUES IN TABLE
        d.execute("INSERT INTO Holder VALUES(:h_id,:h_passw,:h_email,:h_name,:h_type)",
                  {
                      'h_id': h_id.get(),
                      'h_passw': h_passw.get(),
                      'h_email': h_email.get(),
                      'h_name': h_name.get(),
                      'h_type': h_type.get(),

                  }

                  )

        conn.commit()
        conn.close()

        # clear text boxes
        h_id.delete(0, END)
        h_passw.delete(0, END)
        h_email.delete(0, END)
        h_name.delete(0, END)
        h_type.delete(0, END)

    #############################
    h_id = Entry(top, width=30).grid(row=1, column=2, padx=20)
    h_passw = Entry(top, width=30).grid(row=2, column=2, padx=20)
    h_email = Entry(top, width=30).grid(row=3, column=2, padx=20)
    h_name = Entry(top, width=30).grid(row=4, column=2, padx=20)
    h_type = Entry(top, width=30).grid(row=5, column=2, padx=20)

    h_id_label = Label(top, text="ID").grid(row=1, column=1, padx=20)
    h_passw_label = Label(top, text="Password").grid(row=2, column=1, padx=20)
    h_email_label = Label(top, text="email").grid(row=3, column=1, padx=20)
    h_name_label = Label(top, text="Name").grid(row=4, column=1, padx=20)
    h_type_label = Label(top, text="Type").grid(row=5, column=1, padx=20)

    ##########
    # submit button
    submit_btn = Button(top, text="Create Account!", command=submit).grid(row=6, column=1, columnspan=2, pady=10,
                                                                          padx=10, ipadx=100)

