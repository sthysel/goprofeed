from goprocam import GoProCamera, constants

gopro = GoProCamera.GoPro(constants.gpcontrol)
gopro.stream(
    'udp://127.0.0.1:10000',
    quality='medium',
)

