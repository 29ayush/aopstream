import datetime

timeString = "173521_03703"
hourInit = int(timeString[:2])
minuteInit = int(timeString[2:4])
secondInit = int(timeString[4:6])
chunkStart = int(timeString[ 7:])
link = lambda count : "https://sportspreview.akamaized.net/ipl/2021/master/720/20211004/%s.ts?hdntl=exp=1633454851~acl=/*~data=hdntl~hmac=d15a2a02b178d0fd1a281f8588fb9d3c7c3ae750f115ed3138f2c89224a418c5" % count

maxTime = datetime.datetime.now( datetime.timezone.utc).strftime("%H%M%S" )
count = ""
i = 0 
with open( "aop.m3u8", "w") as f:
    f.write( "#EXTM3U\n#EXT-X-TARGETDURATION:8\n#EXT-X-PLAYLIST-TYPE:VOD\n#EXT-X-VERSION:3\n#EXT-X-MEDIA-SEQUENCE:20\n" )
    while count < maxTime :
        totalSeconds = secondInit + 4 * i
        seconds = totalSeconds % 60
        totalMinutes = minuteInit + ( totalSeconds // 60 ) 
        minute = totalMinutes % 60
        totalHours = hourInit + ( totalMinutes // 60 ) 
        hour = totalHours % 24
        tim = str( hour ).zfill(2) + str( minute ).zfill(2) + str ( seconds ).zfill( 2 )  
        count = "%s_%s" % (tim, str(chunkStart + i).zfill(5 ) )
        f.write( "#EXTINF:4.00000,\n" )
        #print( count ) 
        f.write( link( count )  + "\n" )
        i = i + 1
