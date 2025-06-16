def k_and_m_into_int(text):
    text = text.replace(',', '')
    
    if 'K' in text:
        text = text.replace('K', '')
        if '.' in text:
            return int(float(text) * 1000)
        return int(text) * 1000
    elif 'M' in text:
        text = text.replace('M', '')
        if '.' in text:
            return int(float(text) * 1000000)
        return int(text) * 1000000
    else:
        if '.' in text:
            return int(float(text))
        return int(text)