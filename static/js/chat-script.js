var initialData = [
    { firstName: "Danny", lastName: "LaRusso", phones: [
        { type: "Mobile", number: "(555) 121-2121" },
        { type: "Home", number: "(555) 123-4567"}]
    },
    { firstName: "Sensei", lastName: "Miyagi", phones: [
        { type: "Mobile", number: "(555) 444-2222" },
        { type: "Home", number: "(555) 999-1212"}]
    }
];
 
// var ContactsModel = function() {
//     var self = this;
//     self.contacts = ko.observableArray();
//     self.users = ko.observableArray();
//
//     self.addMessage = function (formElement) {
//         console.log(formElement);
//     };
// };

var ContactsModel = {
    messages: ko.observableArray(),
    users: ko.observableArray(),
    textMessage: ko.observable(),
    addMessage: function (formElement) {
        this.messages.push({
            text: this.textMessage(),
        });
    }
};

ko.applyBindings(ContactsModel);