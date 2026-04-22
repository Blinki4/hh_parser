from utils.chunks_manager import ChunksManager

class TestChunksManager:
    CHUNKS_COUNT = 4

    def test_split_chunks_without_remainder(self):
        array = list(range(20))
        chunks = ChunksManager.split_list_into_chunks(array, self.CHUNKS_COUNT)
        assert len(chunks) == self.CHUNKS_COUNT

    def test_split_chunks_with_remainder(self):
        array = list(range(21))
        chunks = ChunksManager.split_list_into_chunks(array, self.CHUNKS_COUNT)
        assert len(chunks) == self.CHUNKS_COUNT + 1

    def test_split_chunks_with_empty_array(self):
        array = []
        chunks = ChunksManager.split_list_into_chunks(array, self.CHUNKS_COUNT)
        assert len(chunks) == 0

    def test_join_chunks(self):
        chunks = [
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8]
        ]
        joined = ChunksManager.join_chunks(chunks)
        assert len(joined) == 9

    def test_join_chunks_with_remainder(self):
        chunks = [
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8],
            [9]
        ]
        joined = ChunksManager.join_chunks(chunks)
        assert len(joined) == 10

    def test_join_empty_array(self):
        chunks = []
        joined = ChunksManager.join_chunks(chunks)
        assert len(joined) == 0

    def test_join_empty_chunks(self):
        chunks = [[],[],[],[]]
        joined = ChunksManager.join_chunks(chunks)
        assert len(joined) == 0