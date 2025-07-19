from pydantic import BaseModel, field_validator, ValidationError

class User_Profile(BaseModel):
    username: str
    email: str
    age: int

    @field_validator("email")
    def validate_email(cls, value):
        if "@" not in value or "." not in value.split("@")[-1]:
            raise ValueError("Invalid email format")
        return value

    @field_validator("age")
    def validate_age(cls, value):
        if value <= 18 or value >= 100:
            raise ValueError("You are not eligible")
        return value
    
    def display_profile(self):
        return(
            f"Username: {self.username}\n"
            f"Email: {self.email}\n"
            f"Age: {self.age}\n"
            f"Profile created successfully!"
        )

# Example usage
try:
    username = input("Enter your username: ")
    email = input("Enter your email: ")
    age_input = input("Enter your age: ")
    
    # Convert age to int for validation
    profile = User_Profile(
        username=username,
        email=email,
        age=age_input
    )

    print(profile.display_profile())

except ValidationError as e:
    for error in e.errors():
        print(f" {error['loc'][0]}: {error['msg']}")


