class ContactList:

    def __init__(self, group_type):
        self.group_name = group_type
        self.group_type = group_type
        self.group_type = []
    
    def appending_contacts(self, name, number):
        self.group_type.append({"name": name, "number": number})
        print(f"{name} has been added to your {self.group_name} contact list")

    def add_contact(self, name, number):
            self.appending_contacts(name, number)
            list.sort(self.group_type, key=lambda contact: contact['name'])
        
        # IMPROVEMENETS to work on
        # - Getting issues where it still goes through the if statement enven though it is false. 
        # - It also adds last entry twice
        # if self.group_type:
        #     for contact in self.group_type:
        #         if name == contact['name']:
        #             print('>>>>>>>>>>>>',name == contact['name'])
        #             print('>>>>>>>>>>>>',name, contact['name'])
        #             print('Contact Name already in your list!')
        #             (sorted(self.group_type, key=lambda x: x['name']))
        #         # else:
        #         #     self.appending_contacts(name, number)
        # else:
        #     self.appending_contacts(name, number)

    def remove_contact(self, name):
        for contact in self.group_type:
            if contact['name'] == name:
                contact_index = self.group_type.index(contact)
                del self.group_type[contact_index]
                print(f"{contact['name']} has been succesfully removed from your contact list")

    def find_shared_contacts(self, contacts_list):
        shared_contacts = ContactList('shared_contacts')
        for contact in self.group_type:
            for contact_two in contacts_list:
                if contact['name'] == contact_two['name'] and contact['number'] == contact_two['number']:
                    shared_contacts.appending_contacts(contact['name'], contact['number'])
                    print('SHARED CONTACTS: ',shared_contacts.group_type)




friends = ContactList('friends')
friends.add_contact('Michael', '111-111-1111')
# friends.add_contact('Michael', '222-222-2222')
# friends.add_contact('Robert', '222-222-2222')
# friends.add_contact('Alice', '333-333-3333')
# friends.add_contact('Mary', '444-444-4444')


friends.remove_contact('Michael')

work_buddies = ContactList('friends')
work_buddies.add_contact('John', '444-444-4444')
# work_buddies.add_contact('Jaime', '555-555-5555')
# work_buddies.add_contact('Karen', '666-666-6666')
# work_buddies.add_contact('Mary', '444-444-4444')



my_friends_list = friends.group_type
my_work_buddies_list = work_buddies.group_type
friends_i_work_with = friends.find_shared_contacts(my_work_buddies_list)    

