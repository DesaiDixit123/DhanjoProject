from django.http import JsonResponse
from django_countries import countries
from cities_light.models import Region,City


def get_countries(request):
    # Fetching all countries as a list of dictionaries with code and name
    country_list = [{"code": code, "name": name} for code, name in list(countries)]
   
    return JsonResponse(country_list, safe=False)


def get_states_by_country(request, country_name):
    try:
        country_code = None
        for code, name in countries:
            if name.lower() == country_name.lower():
                country_code = code
                break

        if not country_code:
            return JsonResponse({"error": "Invalid country name"}, status=400)

        # Filter regions using the found country code
        regions = Region.objects.filter(country__code2=country_code)
        states = [{"id": region.id, "name": region.name} for region in regions]  # Use 'id' for unique state identifiers
       
        return JsonResponse(states, safe=False)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


def get_cities_by_state(request, state_id):
    try:
      
        state = Region.objects.filter(id=state_id).first()
        print(f"State: {state}") 

        if not state:
            return JsonResponse({"error": f"Invalid state ID: {state_id}"}, status=400)
      
        cities = City.objects.filter(region=state_id)

        print(f"Cities: {cities}") 
    
        if not cities.exists():
            return JsonResponse([], safe=False)


        city_list = [{"id": city.id, "name": city.name} for city in cities]
        # print(f"Cities: {city_list}")
        return JsonResponse(city_list, safe=False)

    except Exception as e:
        return JsonResponse({"error": f"Internal server error: {str(e)}"}, status=500)