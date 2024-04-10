from PIL import Image, ImageDraw, ImageFont
from getQR import generate_qr_code 

def draw_ticket_details(background_image_path, booked_from, start_date, boarding_at, departure_date,
                        booked_to, arrival_date, train_number, train_name, train_class, quota,
                        distance, booking_date, passenger_name, age, gender, status,
                        fare, service_charge, total, output_image_path):
    img = Image.open(background_image_path)
    draw = ImageDraw.Draw(img)


    font = ImageFont.truetype('NotoSans-Medium.ttf', 48)
    fontSmall = ImageFont.truetype('NotoSans-Medium.ttf', 40)
    fontXs = ImageFont.truetype('NotoSans-Medium.ttf', 36)
    fontBold = ImageFont.truetype('NotoSans-Bold.ttf', 45)
    fontSmallBold = ImageFont.truetype('NotoSans-Bold.ttf', 40)

    # Booked From And To
    draw.text((200, 510), booked_from, (0, 0, 0), font=font)
    draw.text((180, 575), start_date, (0, 0, 0), font=fontSmall)

    draw.text((1700, 510), booked_to, (0, 0, 0), font=font)
    draw.text((1650, 575), arrival_date, (0, 0, 0), font=fontSmall)

    # Boarding Details
    draw.text((920, 510), boarding_at, (0, 0, 0), font=fontBold)
    draw.text((820, 575), departure_date, (0, 0, 0), font=fontSmallBold)

    # Train Details
    draw.text((220, 720), train_number, ('#007EB9'), font=fontBold)
    draw.text((885, 720), train_name, ('#007EB9'), font=fontBold)
    draw.text((1820, 720), train_class, ('#007EB9'), font=fontBold)

    draw.text((200, 850), quota, (0, 0, 0), font=fontXs)
    draw.text((1080, 850), distance, (0, 0, 0), font=fontXs)
    draw.text((1750, 850), booking_date, (0, 0, 0), font=fontXs)

    # Passenger Details
    draw.text((110, 1050), passenger_name, (0, 0, 0), font=fontSmall)
    draw.text((625, 1050), age, (0, 0, 0), font=fontSmall)
    draw.text((830, 1050), gender, (0, 0, 0), font=fontSmall)
    draw.text((1030, 1050), status, (0, 0, 0), font=fontSmall)
    draw.text((1640, 1050), status, (0, 0, 0), font=fontSmall)

    # Price Details
    draw.text((900, 1410), fare, (0, 0, 0), font=fontXs)
    draw.text((330, 2760), fare, (0, 0, 0), font=fontXs)  # Taxable Value

    draw.text((900, 1470), service_charge, (0, 0, 0), font=fontXs)
    draw.text((900, 1530), total, (0, 0, 0), font=fontXs)

    qr_data = f"""
    PNR
    6653072659
    Transaction ID: 100007586258120
    From 
    {booked_from}
    Departure* {departure_date}To 
    {booked_to}
    Arrival* {arrival_date}Train No./Name 
    {train_number}/{train_name}
    Distance 
    {distance}
    Passenger Details 
    {passenger_name} 
    {age} 
    {gender} 
    {status}
    Payment Details
    Ticket Fare    ₹ {fare}
    IRCTC Convenience Fee (Incl. of GST)    ₹ {service_charge}
    Total Fare (all inclusive)    ₹ {total}
    """
    qr_filename = "ticket_qr.png"
    generate_qr_code(qr_data, qr_filename)

    # Load and paste QR code onto the ticket
    qr_img = Image.open(qr_filename)
    qr_img = qr_img.resize((500, 500))
    img.paste(qr_img, (1600, 1250))  # Adjust the coordinates as per your requirement

    img.save(output_image_path)

# draw_ticket_details("empty.jpeg", "JAMMU TAWI (JAT)", "10-Apr-2024", "22:45", "11-Apr-2024",
#                     "SIWAN (SV)", "23:05", "15652", "LOHIT EXPRESS", "THIRD AC (3A)", "CNF/B437/MIDDLE", "1365KM",
#                     "10-Apr-2024", "GAURAV MISHRA", "18", "M", "CNF", "1985.00", "82.00", "2067.00",
#                     "output_ticket.png")
