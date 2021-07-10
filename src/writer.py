import pandas as pd
from datetime import datetime

class ListsInit(object):
    def __init__(self):
        super(ListsInit, self).__init__()

    @staticmethod
    def meetup_output(data):
        meetup.append(data)


meetup = []


class DataWriter(ListsInit):
    def __init__(self):
        super(DataWriter, self).__init__()

    def main_output(self):
        dfs = {
            'Meetup': pd.DataFrame(meetup)
        }
        # now = datetime.now().strftime('%d-%m-%Y_%H-%M')
        now = 'sample'
        writer = pd.ExcelWriter(f"meetup-output-{now}.xlsx", engine='xlsxwriter')

        # Auto adjust column width, text wrap
        for sheet_name, df in dfs.items():
            df.to_excel(writer, sheet_name=sheet_name, index=False)
            wb = writer.book
            worksheet = writer.sheets[sheet_name]
            text_format = wb.add_format({'text_wrap': True, 'valign': 'top'})

            for idx, col in enumerate(df):
                series = df[col]
                max_len = max((series.astype(str).map(len).max(),
                               len(str(series.name)))) + 1
                if max_len > 100:
                    worksheet.set_column(idx, idx, max_len / 3, text_format)
                else:
                    worksheet.set_column(idx, idx, max_len, text_format)
        writer.save()

    @staticmethod
    def clean_df(list_of_dicts):
        df = pd.DataFrame(list_of_dicts).apply(lambda x: pd.Series(x.dropna().values))
        return df

    @staticmethod
    def clean_data(data):
        clean = [x.strip().replace('\n', '').replace('  ', '').replace('€', '') for x in data]
        clean = list(filter(None, clean))
        clean = ', '.join(clean)
        return clean




