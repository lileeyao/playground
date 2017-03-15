# This script executes a large IO of SQL in transactions of a defined size.
input = StringIO.new((1..20).to_a.join("\n"))

# simulated
def execute_sql(sql)
  puts sql
end

# simulated
def transaction
  execute_sql 'BEGIN'
  yield
  execute_sql 'END'
end

def yield_byte_limit(byte_limit)
  bytes_processed = 0
  while bytes_processed < byte_limit
    data = yield
    break if data.nil?
    bytes_processed += data.bytesize
  end
end

until input.eof?
  transaction do
    yield_byte_limit(10) do
      if line = input.gets
        execute_sql line
      end
      line
    end
  end
end
