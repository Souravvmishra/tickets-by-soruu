from PIL import Image, ImageDraw, ImageFont

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

    img.save(output_image_path)

