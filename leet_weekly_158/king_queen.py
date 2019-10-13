class Solution(object):

    def queensAttacktheKing(self, queens, king):
        mat = [[0 for i in range(8)] for j in range(8)]
        # print (mat)
        for q in queens:
            mat[q[0]][q[1]] = 1
        # print (mat)
        res = []

        #1
        x = king[0] - 1
        y = king[1]
        while( x >= 0 ):
            if mat[x][y] == 1:
                res.append([x, y])
                break
            x -= 1
        #5
        x = king[0] + 1
        y = king[1]
        while(x < 8):
            if mat[x][y] == 1:
                res.append([x, y])
                break
            x += 1

        #3
        x = king[0]
        y = king[1] + 1
        while (y < 8):
            if mat[x][y] == 1:
                res.append([x, y])
                break
            y += 1

        #7
        x = king[0]
        y = king[1] - 1
        while (y >= 0):
            if mat[x][y] == 1:
                res.append([x, y])
                break
            y -= 1

        #2
        x = king[0] - 1
        y = king[1] + 1
        while (x >= 0 and y < 8):
            if mat[x][y] == 1:
                res.append([x, y])
                break
            y += 1
            x -= 1

        # 4
        x = king[0] + 1
        y = king[1] + 1
        while (x < 8 and y < 8):
            if mat[x][y] == 1:
                res.append([x, y])
                break
            y += 1
            x += 1

        # 6
        x = king[0] + 1
        y = king[1] - 1
        while (x < 8 and y >= 0):
            if mat[x][y] == 1:
                res.append([x, y])
                break
            y -= 1
            x += 1

        #8
        x = king[0] - 1
        y = king[1] - 1
        while (x >= 0 and y >= 0):
            if mat[x][y] == 1:
                res.append([x, y])
                break
            y -= 1
            x -= 1

        return res

print (Solution().queensAttacktheKing([[5,6],[7,7],[2,1],[0,7],[1,6],[5,1],[3,7],[0,3],[4,0],[1,2],[6,3],[5,0],[0,4],[2,2],[1,1],[6,4],[5,4],[0,0],[2,6],[4,5],[5,2],[1,4],[7,5],[2,3],[0,5],[4,2],[1,0],[2,7],[0,1],[4,6],[6,1],[0,6],[4,3],[1,7]],[3,4]))