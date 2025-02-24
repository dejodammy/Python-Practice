with open("F:\downloads\Mail+Merge+Project+Start\Mail Merge Project Start\Input\Letters\starting_letter.txt") as letter_file:
    with open(r"F:\downloads\Mail+Merge+Project+Start\Mail Merge Project Start\Input\Names\invited_names.txt") as Names:
        people = Names.readlines()
        dejo = letter_file.read()
        for x in people:
            x = x.strip()
            new_letter = dejo.replace("[name]",x)
            file_path = "F:\downloads\Mail+Merge+Project+Start\Mail Merge Project Start\Output\ReadyToSend"
            with open(f"{file_path}\\{x}.txt", "w") as new_message:
                new_message.write(new_letter)
                