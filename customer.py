

class Customer:
    def __init__(self, customer_id: str, name: str, email: str, phone: str):
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.phone = phone

    def get_info(self) -> str:
        return (f"Customer ID: {self.customer_id}\nName: {self.name}\n"
                f"E-Mail: {self.email}\nPhone: {self.phone}")

    def update_contact(self, email: str = None, phone: str = None):
        if email:
            self.email = email
        if phone:
            self.phone = phone

    def to_dict(self) -> dict:
        return {
            "customer_id": self.customer_id,
            "name": self.name,
            "email": self.email,
            "phone": self.phone
        }

    def __str__(self) -> str:
        return self.get_info()
