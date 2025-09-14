#!pip install -qU dspy pydantic

# Build AI Agents with DSPy

## Define Data Structure
from pydantic import BaseModel

class Date(BaseModel):
    # Somehow LLM is bad at specifying `datetime.datetime`, so
    # we define a custom class to represent the date.
    year: int
    month: int
    day: int
    hour: int

class UserProfile(BaseModel):
    user_id: str
    name: str
    email: str

class Flight(BaseModel):
    flight_id: str
    date_time: Date
    origin: str
    destination: str
    duration: float
    price: float

class Itinerary(BaseModel):
    confirmation_number: str
    user_profile: UserProfile
    flight: Flight

class Ticket(BaseModel):
    user_request: str
    user_profile: UserProfile

## Create Dummy Data
user_database = {
    "Adam": UserProfile(user_id="1", name="Adam", email="adam@gmail.com"),
    "Bob": UserProfile(user_id="2", name="Bob", email="bob@gmail.com"),
    "Chelsie": UserProfile(user_id="3", name="Chelsie", email="chelsie@gmail.com"),
    "David": UserProfile(user_id="4", name="David", email="david@gmail.com"),
}

flight_database = {
    "DA123": Flight(
        flight_id="DA123",  # DSPy Airline 123
        origin="SFO",
        destination="JFK",
        date_time=Date(year=2025, month=9, day=1, hour=1),
        duration=3,
        price=200,
    ),
    "DA125": Flight(
        flight_id="DA125",
        origin="SFO",
        destination="JFK",
        date_time=Date(year=2025, month=9, day=1, hour=7),
        duration=9,
        price=500,
    ),
    "DA456": Flight(
        flight_id="DA456",
        origin="SFO",
        destination="SNA",
        date_time=Date(year=2025, month=10, day=1, hour=1),
        duration=2,
        price=100,
    ),
    "DA460": Flight(
        flight_id="DA460",
        origin="SFO",
        destination="SNA",
        date_time=Date(year=2025, month=10, day=1, hour=9),
        duration=2,
        price=120,
    ),
}

itinery_database = {}
ticket_database = {}

## Define the Tools

import random
import string


def fetch_flight_info(date: Date, origin: str, destination: str):
    """Fetch flight information from origin to destination on the given date"""
    flights = []

    for flight_id, flight in flight_database.items():
        if (
            flight.date_time.year == date.year
            and flight.date_time.month == date.month
            and flight.date_time.day == date.day
            and flight.origin == origin
            and flight.destination == destination
        ):
            flights.append(flight)
    if len(flights) == 0:
        raise ValueError("No matching flight found!")
    return flights

def fetch_itinerary(confirmation_number: str):
    """Fetch a booked itinerary information from database"""
    return itinery_database.get(confirmation_number)


def pick_flight(flights: list[Flight]):
    """Pick up the best flight that matches users' request. we pick the shortest, and cheaper one on ties."""
    sorted_flights = sorted(
        flights,
        key=lambda x: (
            x.get("duration") if isinstance(x, dict) else x.duration,
            x.get("price") if isinstance(x, dict) else x.price,
        ),
    )
    return sorted_flights[0]


def _generate_id(length=8):
    chars = string.ascii_lowercase + string.digits
    return "".join(random.choices(chars, k=length))


def book_flight(flight: Flight, user_profile: UserProfile):
    """Book a flight on behalf of the user."""
    confirmation_number = _generate_id()
    while confirmation_number in itinery_database:
        confirmation_number = _generate_id()
    itinery_database[confirmation_number] = Itinerary(
        confirmation_number=confirmation_number,
        user_profile=user_profile,
        flight=flight,
    )
    return confirmation_number, itinery_database[confirmation_number]


def cancel_itinerary(confirmation_number: str, user_profile: UserProfile):
    """Cancel an itinerary on behalf of the user."""
    if confirmation_number in itinery_database:
        del itinery_database[confirmation_number]
        return
    raise ValueError("Cannot find the itinerary, please check your confirmation number.")


def get_user_info(name: str):
    """Fetch the user profile from database with given name."""
    return user_database.get(name)


def file_ticket(user_request: str, user_profile: UserProfile):
    """File a customer support ticket if this is something the agent cannot handle."""
    ticket_id = _generate_id(length=6)
    ticket_database[ticket_id] = Ticket(
        user_request=user_request,
        user_profile=user_profile,
    )
    return ticket_id

## Create ReAct Agent
import dspy

class DSPyAirlineCustomerService(dspy.Signature):
    """You are an airline customer service agent that helps user book and manage flights.

    You are given a list of tools to handle user request, and you should decide the right tool to use in order to
    fulfill users' request."""

    user_request: str = dspy.InputField()
    process_result: str = dspy.OutputField(
        desc=(
                "Message that summarizes the process result, and the information users need, e.g., the "
                "confirmation_number if a new flight is booked."
            )
        )

agent = dspy.ReAct(
    DSPyAirlineCustomerService,
    tools = [
        fetch_flight_info,
        fetch_itinerary,
        pick_flight,
        book_flight,
        cancel_itinerary,
        get_user_info,
        file_ticket,
    ]
)

## Use the Agent
import os
LLM_API_KEY = os.environ.get("GEMINI_API_KEY")

import dspy

lm = dspy.LM("gemini/gemini-2.5-flash", api_key=LLM_API_KEY)
dspy.configure(lm=lm)

result = agent(user_request="please help me book a flight from SFO to JFK on 09/01/2025, my name is Adam")
print(result)

