from fastapi import APIRouter, Depends, HTTPException
from fastapi.routing import APIRoute, url_path_for
import httpx

router = APIRouter(route_class=APIRoute)


@router.get("/oauth/callback")
async def oauth_callback(code: str):
    # Handle the OAuth callback
    # Extract the authorization code from the query parameters

    # Make a POST request to obtain the access token
    access_token = await get_access_token(code)
    
    # Use the access token to make API calls or store it for future use
    
    return {"access_token": access_token}


async def get_access_token(code: str):
    # Make a POST request to obtain the access token using the code
    
    # Construct the request URL and payload
    token_url = "https://connect.squareup.com/oauth2/token"
    payload = {
        "client_id": "YOUR_CLIENT_ID",
        "client_secret": "YOUR_CLIENT_SECRET",
        "code": code,
        "grant_type": "authorization_code",
        "redirect_uri": url_path_for("oauth_callback"),
    }
    
    async with httpx.AsyncClient() as client:
        response = await client.post(token_url, data=payload)
        if response.status_code == 200:
            data = response.json()
            access_token = data.get("access_token")
            return access_token
        else:
            raise HTTPException(status_code=response.status_code, detail="Failed to obtain access token")


@router.get("/oauth/authorize")
async def oauth_authorize():
    # Generate the authorization URL
    
    # Construct the authorization URL
    authorize_url = "https://connect.squareup.com/oauth2/authorize"
    params = {
        "client_id": "YOUR_CLIENT_ID",
        "response_type": "code",
        "redirect_uri": url_path_for("oauth_callback"),
    }
    authorization_url = f"{authorize_url}?{httpx.URLParams(params)}"
    
    return {"authorization_url": authorization_url}
