json.extract! user, :id, :name, :rut, :created_at, :updated_at
json.url user_url(user, format: :json)
