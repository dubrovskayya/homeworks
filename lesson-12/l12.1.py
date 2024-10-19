
import pandas as pd
import requests

mykey='zNU32wVYY57UhiycDRQsbdUsOt2rC4nyHMTv6PMC'
url=f'https://api.nasa.gov/neo/rest/v1/neo/browse?api_key={mykey}'

def api_open(url):
    response=requests.get(url)
    if response.status_code == 200:
        data=response.json()
        info=data['near_earth_objects']

        obj_df=pd.DataFrame([{
            'Name':'test',
            'Potential danger':'test',
            'Date of the closest approach':'test',
            'Orbiting body':'test'
        }])
    #без фильтрации
    #'''
        for current_dict in info:
            if current_dict['is_potentially_hazardous_asteroid']:
                danger='danger is possible'
            else:
                danger='no danger'
            x={'Name':current_dict['name'],
            'Potential danger':danger,
            'Date of the closest approach':current_dict['close_approach_data'][0]['close_approach_date_full'],
            'Orbiting body': current_dict['close_approach_data'][0]['orbiting_body']}
            obj_df = pd.concat([obj_df, pd.DataFrame([x])], ignore_index=True)

        obj_df.drop(index=0, inplace=True)
        #print(obj_df)
        obj_df.to_excel('cosmo.xlsx',index=False)
    else:
        print('cant open the url')
    #'''
    # с фильтрацией
    '''
        for current_dict in info:
            if  current_dict['close_approach_data'][0]['orbiting_body']=='Earth':
                if current_dict['is_potentially_hazardous_asteroid']:
                    danger='danger is possible'
                else:
                    danger='no danger'
                x={'Name':current_dict['name'],
                'Potential danger':danger,
                'Date of the closest approach':current_dict['close_approach_data'][0]['close_approach_date_full'],
                'Orbiting body': current_dict['close_approach_data'][0]['orbiting_body']}
                obj_df = pd.concat([obj_df, pd.DataFrame([x])], ignore_index=True)
         obj_df.drop(index=0, inplace=True)
        #print(obj_df)
        obj_df.to_excel('cosmo.xlsx',index=False)
    else:
        print('cant open the url')
    '''

api_open(url)

