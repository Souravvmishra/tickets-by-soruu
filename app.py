from flask import Flask, render_template, request, send_file
from newTicketAtul import draw_ticket_details

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Retrieve data from the form
        booked_from = request.form["booked_from"]
        boarding_at = request.form["boarding_at"]
        booked_to = request.form["booked_to"]
        start_date = request.form["start_date"]
        boarding_departure = request.form["boarding_departure"]
        arrival_date = request.form["arrival_date"]
        pnr = request.form["pnr"]
        train_name = request.form["train_name"]
        train_class = request.form["train_class"]
        quota = request.form["quota"]
        distance = request.form["distance"]
        booking_date = request.form["booking_date"]
        passenger_name = request.form["passenger_name"]
        gender = request.form["gender"]
        age = request.form["age"]
        status = request.form["status"]
        fare = request.form["fare"]
        service_charge = request.form["service_charge"]
        total = request.form["total"]
        
        # Call draw_ticket_details function with the retrieved data
        generated_image_path = 'output_image_path.jpg'  # Define the path where the generated image will be saved
        draw_ticket_details(
            background_image_path='empty.jpeg',
            booked_from=booked_from,
            start_date=start_date,
            boarding_at=boarding_at,
            departure_date=boarding_departure,
            booked_to=booked_to,
            arrival_date=arrival_date,
            train_number=pnr,
            train_name=train_name,
            train_class=train_class,
            quota=quota,
            distance=distance,
            booking_date=booking_date,
            passenger_name=passenger_name,
            age=age,
            gender=gender,
            status=status,
            fare=fare,
            service_charge=service_charge,
            total=total,
            output_image_path=generated_image_path
        )
        
        # Return the generated image file as a response
        return send_file(generated_image_path, mimetype='image/jpeg')
                               
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
