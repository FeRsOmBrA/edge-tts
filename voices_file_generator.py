import edge_tts
import asyncio
import csv

async def all_voices():
    voices = await edge_tts.list_voices()
    return voices

async def generate_csv():
    voices = await all_voices()

    header = ['SuggestedCodec', 'FriendlyName', 'Status', 'VoiceTag', 'Name', 'Locale', 'ShortName', 'Gender']
    rows = []

    for voice in voices:
        row = [
            voice['SuggestedCodec'],
            voice['FriendlyName'],
            voice['Status'],
            '',  # VoiceTag is empty in the provided data
            voice['Name'],
            voice['Locale'],
            voice['ShortName'],
            voice['Gender']
        ]
        rows.append(row)

    with open('output.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(rows)

if __name__ == "__main__":
    asyncio.run(generate_csv())
