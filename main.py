import os
import logging
import sys
import re
import smtplib

# port defines the port used by the api server
port = os.getenv("PORT", "8080")
sourceAddr = os.getenv("SOURCE_ADDR", "admin@gmail.com")


def main() {
    # // Declare the router
    e = echo.New()
    e.Use(middleware.Logger())
    e.Use(middleware.Recover())

    # // Define the API Services
    v: = verifier.NewVerifier(retrievePTR(), sourceAddr)

    # // Bind the API endpoints to router
    e.GET("/v1/:format/:email", api.LookupHandler(v), authMiddleware)
    e.GET("/v1/health", api.HealthHandler(), authMiddleware)

    # // Listen and Serve
    e.Logger.Fatal(e.Start(":" + port))
}
