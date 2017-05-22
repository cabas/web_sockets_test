class SomethingChannel < ApplicationCable::Channel
  def subscribed
    # stream_from "some_channel"
  end

  def unsubscribed
    # Any cleanup needed when channel is unsubscribed
  end

  def register_attendance (data)
  	user = User.find_by(name: data["username"])
  	attendance = Attendance.create(user: user, date: Date.parse(data["date"]))
  	user.attendances << attendance
  	user.save
  	return "attendance saved"
  end

  def write (input)
  	puts input
  end
end
