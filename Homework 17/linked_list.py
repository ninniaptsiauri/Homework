# ვქმნის კლასს Node-ს, linked list-ის თითოეული კვანძისთვის
class Node: 
    def __init__(self, data=None): # აღვწერთ init-ს რომ გააკეთოს data-ს და next-ის ინიციალიზაცია(ატრიბუტად ვიღებთ მხოლოდ data-ს)
        self.data = data # data-ს ინნიციალიზაცია და მონაცემების შენახვა  data-ში
        self.next = None  # შემდეგი ობიექტის მდებაორეობა იქნება None, რადგან ლისტი შესაძლოა იყოს ერთელემენტიანი


# ვქმნის ახალ კლასს, რომელსაც ექნება მეთოდები და ზემოქმედებას განახორციელებს 'Node' კლასზე
class LinkedList:
    def __init__(self): # linked list-ს აუცილებლად უნდა ჰქონდეს self, რადგან linked list-ს შექმნისას მაშინვე უნდა შეიქმნას head, პირველი ელემენტი 
        self.head = None # head ატრიბუტი თავდაპირველად იქნება None, თუ არ მივანიჭებთ რაიმე მნიშვნელობას

    # ვქმნით დამატების მეთოდს, რომელიც ელემენტს დაამატებს ლისტის ბოლოს
    def append(self, data): # append-მა უნდა მიიღოს ახალი ელემენტი, რომელიც იქნება data
        new_node = Node(data) # ვქმნით ახალ ნოუდს, რომელიც არის 'Node' კლასის ობიექტი და მისი მნიშვნელობა არის data
        if self.head is None: # ვამოწმებთ head-ს, თუ ელემენტი არაა დამატებული, ესეიგი არის None
            self.head = new_node # პირველი ელემენტი გახდება head
            return # ვაჩერებთ მეთოდს

        last_node = self.head # სიის ბოლოს ნოუდს ვინახავთ ცვლადში და ვუტოლებთ self.head-ს რომ შევძლოთ while ციკლის გამოყენება
        while last_node.next: # სანამ last-nodeს ექნება next მნიშვნელობა
            last_node = last_node.next # ბოლო ელემენტი გახდება მისი შემდეგი ელემენტი, სანამ არ მივალთ ბოლო ელემენტამდე, რომელსაც არ ექნება next

        last_node.next = new_node # ნაპოვნი ბოლო ელემენტის(რომლის next არის null) next-ში ვამატებთ ახალ ნოუდს


    # ვქმნით წაშლის მეთოდს, ინდექსის მიხედვით
    def remove_at(self, index): # ატრიბუტად მიიღებს index-ს, რადგან წაშლა უნდა მოხდეს ინდექსის მიხედვით
        if index < 0 and self.head is None: # ვამოწმებთ გადაცემული ინდექსი არის თუ არა 0-ზე ნაკლები და ლისტი არის თუ არა ცარიელი
            return # ვაჩერებთ მეთოდს

        if index == 0: # ვამოწმებთ თუ index არის 0, ანუ პირველი ელემენტია
            self.head = self.head.next # პირველ ელემენტს ვცვლით მისი შემდეგი ელემენტის მნიშვნელობით
            return # ვაჩერებთ მეთოდს, რომ აღარ გაგრძელდეს მოქმედება

        current_node = self.head # ვქმნით ცვლადს, დასაფიქსირებლად თუ რომელ ნოუდზე ვიმყოფებით და თავიდან ეს იქნება პირველი ელემენტი
        current_position = 0 # self.head-ის ინდექსი იქნება 0, რადგან პირველი ელემენტია

        while current_node.next and current_position < index - 1: # ვიწყებთ ციკლს, სანამ არსებობს შემდეგი node და პოზიცია არ არის იმ ინდექსზე, რომელსაც ვეძებთ
            current_node = current_node.next # current_node ხდება მისი შემდეგი ელემენტი
            current_position += 1 # პოზიციას ვზრდით ერთით

        if current_node.next: # ვამოწმებთ თუ არსებობს current_node-ის შემდეგი ელემენტი
            current_node.next = current_node.next.next # ნექსთი გახდება შემდეგი ელემენტის შემდეგი მნიშვნელობა


    # ვქმნით დაბეჭდვის ფუნქციონალს, რომ დავინახოთ აღწერილი ფუნქციების შედეგი
    def display(self): # არ გადავცემთ ატრიბუტს
        current_node = self.head # ვქმნით ახალ ცვლადს, რომელსაც ვუტოლებთ სიის პირველ ელემენტს
        while current_node is not None: # while ციკლი თითოეული ელემენტის დასაბეჭდად, სანამ current_node არ იქნება None
            print(current_node.data, end=' -> ') # ვბეჭდავთ current-nodeს data-ს, ვცვლით 'end'-ს მნიშვნელობას ბეჭდვის დროს
            current_node = current_node.next # ცვლადის მნიშვნელობა გახდება მისი შემდეგი node-ის მნიშვნელობა ყოველ ჯერზე


linked_list = LinkedList() # ვქმნით LinkedList-ის ობიექტს

#ვიძახებთ linked.list-დან append-ს და გადავცემთ data-ს
linked_list.append(10) 
linked_list.append(5)
linked_list.append(25)
linked_list.append(12)
linked_list.append(11)

linked_list.display() # linked_list-დან ვიძახებთ display-ს, დასაბეჭდად
print() # პრინტი ბეჭდვისას ახალ ხაზზე გადასასვლელად
linked_list.remove_at(2) # ვიძახებთ linked.list-დან ინდექსით წაშლის მეთოდს და გადავცემთ ინდექსს
linked_list.display() # ვიძახებთ display-ს, დასაბეჭდად
print() # პრინტი ბეჭდვისას ახალ ხაზზე გადასასვლელად
linked_list.remove_at(2) # თავიდან ვიძახებთ linked.list-დან ინდექსით წაშლის მეთოდს და გადავცემთ იგივე ინდექსს
linked_list.display() # ვიძახებთ display-ს, დასაბეჭდად