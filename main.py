import phonenumbers
from phonenumbers import geocoder, carrier, timezone, number_type

def obtener_datos_telefono(numero):
    try:
        telefono = phonenumbers.parse(numero)

        if not phonenumbers.is_valid_number(telefono):
            return "El número ingresado no es válido."

        # Obtener información del número
        pais = geocoder.country_name_for_number(telefono, "es")
        ubicacion = geocoder.description_for_number(telefono, "es")
        compania = carrier.name_for_number(telefono, "es")
        tipo_linea = number_type(telefono)  # Tipo de línea
        zona_horaria = timezone.time_zones_for_number(telefono)

        tipos_linea = {
            phonenumbers.PhoneNumberType.MOBILE: "Móvil",
            phonenumbers.PhoneNumberType.FIXED_LINE: "Línea fija",
            phonenumbers.PhoneNumberType.FIXED_LINE_OR_MOBILE: "Línea fija o móvil",
            phonenumbers.PhoneNumberType.TOLL_FREE: "Gratuito",
            phonenumbers.PhoneNumberType.PREMIUM_RATE: "Tarifa premium",
            phonenumbers.PhoneNumberType.SHARED_COST: "Costo compartido",
            phonenumbers.PhoneNumberType.VOIP: "VOIP",
            phonenumbers.PhoneNumberType.PERSONAL_NUMBER: "Número personal",
            phonenumbers.PhoneNumberType.PAGER: "Buscapersonas",
            phonenumbers.PhoneNumberType.UAN: "Número UAN",
            phonenumbers.PhoneNumberType.UNKNOWN: "Desconocido"
        }

        tipo_linea_str = tipos_linea.get(tipo_linea, "Desconocido")

        return f"""
        === Developed By: T. Stark ===

        País: {pais}
        Ubicación: {ubicacion}
        Compañía: {compania}
        Tipo de línea: {tipo_linea_str}
        Zona horaria: {', '.join(zona_horaria)}
        """
    except phonenumbers.phonenumberutil.NumberParseException as e:
        return f"Error: {e}"

numero = input("Ingresa un numero de telefono en formato internacional (ejemplo: +0123456789): ")
print(obtener_datos_telefono(numero))