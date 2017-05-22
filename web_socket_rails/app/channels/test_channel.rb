class TestChannel < ApplicationCable::TestChannel
	def receive_info (info)
		puts info
	end

	def send_info

	end
end