from practicals.prac08.silver_service_taxi import SilverServiceTaxi


def main():
    """Test SilverServiceTaxi."""
    taxi = SilverServiceTaxi("Taxi", 200, 2)
    taxi.drive(18)
    print(taxi)
    print(taxi.get_fare())

main()